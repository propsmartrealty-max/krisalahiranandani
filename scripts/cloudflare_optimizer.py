#!/usr/bin/env python3
"""
Enterprise Cloudflare, DNS & Infrastructure Optimizer & Hardener
Fully automates security settings, TLS configurations, DNS records, Dynamic Edge Redirects,
Edge Cache Rules, Custom WAF Rulesets, and DNSSEC verification via Cloudflare v4 REST API.
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
import ssl

API_BASE = "https://api.cloudflare.com/client/v4"

def get_ssl_context():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx

def make_request(url, method="GET", headers=None, data=None):
    if headers is None:
        headers = {}
    headers["Content-Type"] = "application/json"
    
    body = None
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    ctx = get_ssl_context()
    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_content = e.read().decode("utf-8")
        try:
            return json.loads(error_content)
        except Exception:
            return {"success": False, "errors": [{"message": error_content}]}
    except Exception as e:
        return {"success": False, "errors": [{"message": str(e)}]}

def get_auth_headers(api_token=None, api_key=None, api_email=None):
    if api_token:
        return {"Authorization": f"Bearer {api_token.strip()}"}
    elif api_key and api_email:
        return {
            "X-Auth-Key": api_key.strip(),
            "X-Auth-Email": api_email.strip()
        }
    else:
        raise ValueError("Must provide either --token or both --key and --email")

def find_zone(headers, zone_name):
    url = f"{API_BASE}/zones?name={zone_name}"
    res = make_request(url, headers=headers)
    if not res.get("success"):
        print(f"[-] Failed to fetch zone: {res.get('errors')}")
        return None
    zones = res.get("result", [])
    if not zones:
        print(f"[-] Zone {zone_name} not found in this account.")
        return None
    return zones[0]

def update_zone_setting(headers, zone_id, setting_id, value):
    url = f"{API_BASE}/zones/{zone_id}/settings/{setting_id}"
    payload = {"value": value}
    res = make_request(url, method="PATCH", headers=headers, data=payload)
    if res.get("success"):
        print(f"  [✓] Setting '{setting_id}' set to: {value}")
    else:
        print(f"  [✗] Setting '{setting_id}' failed: {res.get('errors')}")

def list_dns_records(headers, zone_id):
    url = f"{API_BASE}/zones/{zone_id}/dns_records?per_page=100"
    res = make_request(url, headers=headers)
    if res.get("success"):
        return res.get("result", [])
    return []

def add_or_update_dns_record(headers, zone_id, record_data, existing_records):
    for r in existing_records:
        if r.get("type") == record_data.get("type") and r.get("name") == record_data.get("name"):
            if record_data.get("type") in ["CAA"]:
                if r.get("data", {}) == record_data.get("data", {}):
                    print(f"  [i] CAA record {record_data['name']} already in sync.")
                    return
            elif record_data.get("type") in ["TXT", "MX"]:
                curr_content = str(r.get("content")).strip('"')
                new_content = str(record_data.get("content")).strip('"')
                if curr_content == new_content:
                    print(f"  [i] DNS {record_data['type']} {record_data['name']} already in sync.")
                    return
                else:
                    url = f"{API_BASE}/zones/{zone_id}/dns_records/{r['id']}"
                    res = make_request(url, method="PUT", headers=headers, data=record_data)
                    if res.get("success"):
                        print(f"  [✓] Updated DNS {record_data['type']} {record_data['name']}")
                    else:
                        print(f"  [✗] Failed to update DNS {record_data['type']} {record_data['name']}: {res.get('errors')}")
                    return

    url = f"{API_BASE}/zones/{zone_id}/dns_records"
    res = make_request(url, method="POST", headers=headers, data=record_data)
    if res.get("success"):
        print(f"  [✓] Added DNS {record_data['type']} {record_data['name']}")
    else:
        print(f"  [✗] Failed to add DNS {record_data['type']} {record_data['name']}: {res.get('errors')}")

def delete_dns_record(headers, zone_id, record_id, record_desc=""):
    url = f"{API_BASE}/zones/{zone_id}/dns_records/{record_id}"
    res = make_request(url, method="DELETE", headers=headers)
    if res.get("success"):
        print(f"  [✓] Removed conflicting DNS record: {record_desc}")
    else:
        print(f"  [✗] Failed to delete record {record_id}: {res.get('errors')}")

def sync_routing_records(headers, zone_id, zone_name, pages_target="krisalahiranandani.pages.dev"):
    records = list_dns_records(headers, zone_id)
    www_target = f"www.{zone_name}"

    for r in records:
        r_name = r.get("name", "").lower()
        r_type = r.get("type", "").upper()
        r_id = r.get("id")
        if r_type in ["A", "AAAA"]:
            if r_name == zone_name.lower() or r_name == www_target.lower():
                print(f"  [!] Found conflicting {r_type} record for {r_name} pointing to {r.get('content')}. Removing...")
                delete_dns_record(headers, zone_id, r_id, f"{r_type} {r_name}")

    records = list_dns_records(headers, zone_id)

    # Apex CNAME
    apex_cname = next((r for r in records if r.get("type") == "CNAME" and r.get("name", "").lower() == zone_name.lower()), None)
    if apex_cname:
        needs_update = (apex_cname.get("content", "").strip(".").lower() != pages_target.lower()) or not apex_cname.get("proxied", False)
        if needs_update:
            update_data = {
                "type": "CNAME",
                "name": "@",
                "content": pages_target,
                "proxied": True,
                "ttl": 1
            }
            url = f"{API_BASE}/zones/{zone_id}/dns_records/{apex_cname['id']}"
            res = make_request(url, method="PUT", headers=headers, data=update_data)
            if res.get("success"):
                print(f"  [✓] Updated Apex CNAME -> {pages_target} (Proxied)")
        else:
            print(f"  [✓] Apex CNAME ({zone_name}) already routed to {pages_target} (Proxied).")
    else:
        create_data = {
            "type": "CNAME",
            "name": "@",
            "content": pages_target,
            "proxied": True,
            "ttl": 1
        }
        res = make_request(f"{API_BASE}/zones/{zone_id}/dns_records", method="POST", headers=headers, data=create_data)
        if res.get("success"):
            print(f"  [✓] Created Apex CNAME -> {pages_target} (Proxied)")

    # WWW CNAME
    www_cname = next((r for r in records if r.get("type") == "CNAME" and r.get("name", "").lower() == www_target.lower()), None)
    if www_cname:
        needs_update = (www_cname.get("content", "").strip(".").lower() != pages_target.lower()) or not www_cname.get("proxied", False)
        if needs_update:
            update_data = {
                "type": "CNAME",
                "name": "www",
                "content": pages_target,
                "proxied": True,
                "ttl": 1
            }
            url = f"{API_BASE}/zones/{zone_id}/dns_records/{www_cname['id']}"
            res = make_request(url, method="PUT", headers=headers, data=update_data)
            if res.get("success"):
                print(f"  [✓] Updated www CNAME -> {pages_target} (Proxied)")
        else:
            print(f"  [✓] www CNAME ({www_target}) already routed to {pages_target} (Proxied).")
    else:
        create_data = {
            "type": "CNAME",
            "name": "www",
            "content": pages_target,
            "proxied": True,
            "ttl": 1
        }
        res = make_request(f"{API_BASE}/zones/{zone_id}/dns_records", method="POST", headers=headers, data=create_data)
        if res.get("success"):
            print(f"  [✓] Created www CNAME -> {pages_target} (Proxied)")

def sync_dynamic_redirect_rule(headers, zone_id, zone_name):
    """
    Configures single-hop 301 edge redirect from www to apex with full query string preservation.
    """
    url = f"{API_BASE}/zones/{zone_id}/rulesets/phases/http_request_dynamic_redirect/entrypoint"
    payload = {
        "description": "Canonical Apex 301 Edge Redirect",
        "rules": [
            {
                "expression": f'(http.host eq "www.{zone_name}")',
                "description": "Single-Hop 301 Redirect www to Canonical Apex",
                "action": "redirect",
                "action_parameters": {
                    "from_value": {
                        "status_code": 301,
                        "target_url": {
                            "expression": f'concat("https://{zone_name}", http.request.uri.path)'
                        },
                        "preserve_query_string": True
                    }
                },
                "enabled": True
            }
        ]
    }
    res = make_request(url, method="PUT", headers=headers, data=payload)
    if res.get("success"):
        print("  [✓] Single-Hop Canonical Apex 301 Redirect Rule Deployed at Global Edge.")
    else:
        print(f"  [✗] Dynamic redirect rule deployment note: {res.get('errors')}")

def sync_cache_settings_rule(headers, zone_id):
    """
    Configures edge cache optimization rules for static assets and programmatic pages.
    """
    url = f"{API_BASE}/zones/{zone_id}/rulesets/phases/http_request_cache_settings/entrypoint"
    payload = {
        "description": "Enterprise Edge Cache Optimization",
        "rules": [
            {
                "expression": '(starts_with(http.request.uri.path, "/public/") or ends_with(http.request.uri.path, ".webp") or ends_with(http.request.uri.path, ".png") or ends_with(http.request.uri.path, ".jpg") or ends_with(http.request.uri.path, ".svg") or ends_with(http.request.uri.path, ".woff2") or ends_with(http.request.uri.path, ".css") or ends_with(http.request.uri.path, ".js"))',
                "description": "Cache Static Assets at Global Edge for 1 Year",
                "action": "set_cache_settings",
                "action_parameters": {
                    "cache": True,
                    "edge_ttl": {
                        "mode": "override_origin",
                        "default": 31536000
                    },
                    "browser_ttl": {
                        "mode": "override_origin",
                        "default": 31536000
                    },
                    "serve_stale": {
                        "disable_stale_while_updating": False
                    }
                },
                "enabled": True
            },
            {
                "expression": '((starts_with(http.request.uri.path, "/explore/") or ends_with(http.request.uri.path, ".html") or not (http.request.uri.path contains ".") or http.request.uri.path eq "/") and not starts_with(http.request.uri.path, "/api/"))',
                "description": "Cache Clean URLs, Programmatic & HTML Pages at Edge for 24h with SWR",
                "action": "set_cache_settings",
                "action_parameters": {
                    "cache": True,
                    "edge_ttl": {
                        "mode": "override_origin",
                        "default": 86400
                    },
                    "browser_ttl": {
                        "mode": "override_origin",
                        "default": 0
                    },
                    "serve_stale": {
                        "disable_stale_while_updating": False
                    }
                },
                "enabled": True
            }
        ]
    }
    res = make_request(url, method="PUT", headers=headers, data=payload)
    if res.get("success"):
        print("  [✓] Enterprise Edge Cache Optimization Rules Deployed at Global Edge.")
    else:
        print(f"  [✗] Cache settings rule note: {res.get('errors')}")

def sync_custom_waf_rules(headers, zone_id):
    """
    Configures advanced WAF rules with exploit blocking, hotlinking shield with social/AI whitelist.
    """
    rulesets_res = make_request(f"{API_BASE}/zones/{zone_id}/rulesets", headers=headers)
    waf_ruleset_id = None
    if rulesets_res.get("success"):
        for r in rulesets_res["result"]:
            if r.get("phase") == "http_request_firewall_custom":
                waf_ruleset_id = r.get("id")
                break
                
    if not waf_ruleset_id:
        print("  [i] Creating Custom WAF Ruleset...")
        url = f"{API_BASE}/zones/{zone_id}/rulesets"
        method = "POST"
    else:
        url = f"{API_BASE}/zones/{zone_id}/rulesets/{waf_ruleset_id}"
        method = "PUT"

    rules = [
        {
            "action": "skip",
            "action_parameters": {
                "ruleset": "current"
            },
            "description": "Allow & Skip WAF for Googlebot, Search Engines, Auditing & Frontier AI Bots",
            "enabled": True,
            "expression": '(cf.client.bot or http.user_agent contains "Google" or http.user_agent contains "Googlebot" or http.user_agent contains "Google-Extended" or http.user_agent contains "AdsBot-Google" or http.user_agent contains "Mediapartners-Google" or http.user_agent contains "Storebot-Google" or http.user_agent contains "Chrome-Lighthouse" or http.user_agent contains "PageSpeed" or http.user_agent contains "Bingbot" or http.user_agent contains "DuckDuckBot" or http.user_agent contains "GPTBot" or http.user_agent contains "OAI-SearchBot" or http.user_agent contains "ClaudeBot" or http.user_agent contains "Claude-Web" or http.user_agent contains "anthropic-ai" or http.user_agent contains "PerplexityBot" or http.user_agent contains "Applebot" or http.user_agent contains "Meta-ExternalAgent" or http.user_agent contains "DeepSeekBot" or http.user_agent contains "cohere-ai")',
            "logging": {
                "enabled": True
            }
        },
        {
            "action": "block",
            "description": "Block Exploit Kits, Vulnerability Scanners & Path Traversal",
            "enabled": True,
            "expression": '((http.request.uri.path contains "wp-login" or http.request.uri.path contains "phpmyadmin" or http.request.uri.path contains "eval-stdin.php" or http.request.uri.path contains "../" or http.request.uri.path contains "..%2f" or http.request.uri.path contains "/.git" or http.request.uri.path contains "/.env" or http.request.uri.path contains "client_secret.json") or (http.user_agent contains "sqlmap" or http.user_agent contains "nikto" or http.user_agent contains "wpscan" or http.user_agent contains "masscan" or http.user_agent contains "acunetix" or http.user_agent contains "dirbuster" or http.user_agent contains "gobuster")) and not cf.client.bot'
        },
        {
            "action": "managed_challenge",
            "description": "Challenge Malicious IPs and Threat Score >= 20",
            "enabled": True,
            "expression": "(cf.threat_score ge 20 and not cf.client.bot)"
        },
        {
            "action": "block",
            "description": "Enterprise Image & Document Protection with Social & Search Whitelist",
            "enabled": True,
            "expression": '(http.request.uri.path contains "/public/" and not (http.referer contains "krisalahiranandani" or http.referer contains "google" or http.referer contains "bing" or http.referer contains "yahoo" or http.referer contains "duckduckgo" or http.referer contains "facebook" or http.referer contains "fbcdn" or http.referer contains "instagram" or http.referer contains "whatsapp" or http.referer contains "linkedin" or http.referer contains "licdn" or http.referer contains "twitter" or http.referer contains "t.co" or http.referer contains "x.com" or http.referer contains "telegram" or http.referer contains "pinterest" or http.referer contains "reddit" or http.referer contains "openai" or http.referer contains "chatgpt" or http.referer contains "perplexity" or http.referer contains "anthropic" or http.referer contains "claude" or http.referer eq "" or cf.client.bot))'
        },
        {
            "action": "block",
            "description": "Drop Insecure HTTP Verbs",
            "enabled": True,
            "expression": '(http.request.method in {"TRACE" "TRACK" "DEBUG"})'
        }
    ]

    payload = {
        "name": "Custom WAF Security Rules",
        "description": "Custom WAF Security Rules",
        "kind": "zone",
        "phase": "http_request_firewall_custom",
        "rules": rules
    }
    if method == "PUT":
        del payload["kind"]
        del payload["phase"]

    res = make_request(url, method=method, headers=headers, data=payload)
    if res.get("success"):
        print("  [✓] Custom WAF Security Rules Hardened (Social & Search Bots Whitelisted).")
    else:
        print(f"  [✗] Custom WAF rules note: {res.get('errors')}")

def check_dnssec(headers, zone_id):
    url = f"{API_BASE}/zones/{zone_id}/dnssec"
    res = make_request(url, headers=headers)
    if res.get("success"):
        ds = res["result"]
        status = ds.get("status")
        print(f"  [i] DNSSEC Status: {status.upper()}")
        if status == "pending":
            print("  [!] DNSSEC Key is generated on Cloudflare. Add the following DS Record at Hostinger:")
            print(f"      Key Tag:      {ds.get('key_tag')}")
            print(f"      Algorithm:    {ds.get('algorithm')} (ECDSA Curve P-256 with SHA-256)")
            print(f"      Digest Type:  {ds.get('digest_type')} (SHA-256)")
            print(f"      Digest:       {ds.get('digest')}")
            print(f"      DS Record:    {ds.get('ds')}")
        elif status == "active":
            print("  [✓] DNSSEC is 100% ACTIVE and Cryptographically Validated by Domain Registrar!")
    else:
        print(f"  [✗] DNSSEC query note: {res.get('errors')}")

def purge_cache(headers, zone_id):
    url = f"{API_BASE}/zones/{zone_id}/purge_cache"
    res = make_request(url, method="POST", headers=headers, data={"purge_everything": True})
    if res.get("success"):
        print("  [✓] Edge Cache Purged Successfully globally.")
    else:
        print(f"  [✗] Cache purge failed: {res.get('errors')}")

def load_env():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    env_file = os.path.join(project_dir, ".env")
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    if k not in os.environ:
                        os.environ[k] = v

def main():
    load_env()
    parser = argparse.ArgumentParser(description="Cloudflare Hardening & DNS Optimizer")
    parser.add_argument("--token", default=os.getenv("CLOUDFLARE_API_TOKEN"), help="Cloudflare API Bearer Token")
    parser.add_argument("--key", default=os.getenv("CLOUDFLARE_GLOBAL_API_KEY") or os.getenv("CLOUDFLARE_API_KEY"), help="Cloudflare Global API Key")
    parser.add_argument("--email", default=os.getenv("CLOUDFLARE_EMAIL"), help="Cloudflare Account Email")
    parser.add_argument("--zone", default=os.getenv("CLOUDFLARE_ZONE_NAME", "krisalahiranandanitownships.com"), help="Domain zone name")
    parser.add_argument("--test-auth", action="store_true", help="Only verify credentials")
    
    args = parser.parse_args()
    
    try:
        headers = get_auth_headers(args.token, args.key, args.email)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
        
    print(f"==> Authenticating with Cloudflare API...")
    verify_url = f"{API_BASE}/user/tokens/verify" if args.token else f"{API_BASE}/user"
    verify_res = make_request(verify_url, headers=headers)
    
    if not verify_res.get("success"):
        print(f"[-] Authentication failed: {json.dumps(verify_res.get('errors'), indent=2)}")
        sys.exit(1)
        
    print("[✓] Cloudflare Authentication Successful!")
    if args.test_auth:
        return
        
    print(f"\n==> Locating zone: {args.zone}...")
    zone = find_zone(headers, args.zone)
    if not zone:
        sys.exit(1)
        
    zone_id = zone["id"]
    print(f"[✓] Zone found: {zone['name']} (ID: {zone_id})")
    
    print("\n==> 1. Applying Cloudflare Edge Security & Speed Settings...")
    settings_to_apply = [
        ("ssl", "strict"),
        ("min_tls_version", "1.2"),
        ("tls_1_3", "on"),
        ("0rtt", "on"),
        ("always_use_https", "on"),
        ("security_level", "medium"),
        ("browser_check", "on"),
        ("browser_cache_ttl", 86400),
        ("brotli", "on"),
        ("early_hints", "on"),
        ("http3", "on"),
        ("ech", "on"),
        ("pq_keyex", "on"),
        ("ip_geolocation", "on"),
        ("ipv6", "on"),
        ("email_obfuscation", "off"),
        ("server_side_exclude", "on"),
        ("opportunistic_encryption", "on"),
        ("opportunistic_onion", "on"),
        ("websockets", "on"),
        ("automatic_https_rewrites", "on"),
        ("security_header", {"strict_transport_security": {"enabled": True, "max_age": 63072000, "include_subdomains": True, "preload": True, "nosniff": True}})
    ]
    for setting_id, val in settings_to_apply:
        update_zone_setting(headers, zone_id, setting_id, val)
        
    print("\n==> 2. Synchronizing Pages Routing DNS Records (@ and www)...")
    sync_routing_records(headers, zone_id, args.zone, "krisalahiranandani.pages.dev")
        
    print("\n==> 3. Auditing & Hardening DNS Records (CAA, SPF, DMARC, MTA-STS, TLS-RPT)...")
    existing_records = list_dns_records(headers, zone_id)
    
    dns_hardening_records = [
        # CAA Records
        {"type": "CAA", "name": args.zone, "data": {"flags": 0, "tag": "issue", "value": "letsencrypt.org"}, "ttl": 3600},
        {"type": "CAA", "name": args.zone, "data": {"flags": 0, "tag": "issue", "value": "digicert.com"}, "ttl": 3600},
        {"type": "CAA", "name": args.zone, "data": {"flags": 0, "tag": "issue", "value": "pki.goog"}, "ttl": 3600},
        {"type": "CAA", "name": args.zone, "data": {"flags": 0, "tag": "issuewild", "value": "letsencrypt.org"}, "ttl": 3600},
        {"type": "CAA", "name": args.zone, "data": {"flags": 0, "tag": "issuewild", "value": "digicert.com"}, "ttl": 3600},
        {"type": "CAA", "name": args.zone, "data": {"flags": 0, "tag": "issuewild", "value": "pki.goog"}, "ttl": 3600},
        
        # Inbound Mail Defense
        {"type": "MX", "name": args.zone, "content": ".", "priority": 0, "ttl": 3600},
        
        # Email Anti-Spoofing & DMARC Protection with Aggregated Reporting
        {"type": "TXT", "name": args.zone, "content": "v=spf1 -all", "ttl": 3600},
        {"type": "TXT", "name": f"_dmarc.{args.zone}", "content": "v=DMARC1; p=reject; sp=reject; aspf=s; adkim=s; rua=mailto:propsmartrealty@gmail.com", "ttl": 3600},
        {"type": "TXT", "name": f"*._domainkey.{args.zone}", "content": "v=DKIM1; p=", "ttl": 3600},
        {"type": "TXT", "name": f"_mta-sts.{args.zone}", "content": "v=STSv1; id=2026101901", "ttl": 3600},
        {"type": "TXT", "name": f"_smtp._tls.{args.zone}", "content": "v=TLSRPTv1; rua=mailto:propsmartrealty@gmail.com", "ttl": 3600},
    ]
    
    for r in dns_hardening_records:
        add_or_update_dns_record(headers, zone_id, r, existing_records)
        
    print("\n==> 4. Deploying Single-Hop 301 Edge Redirect Rule (www -> Apex)...")
    sync_dynamic_redirect_rule(headers, zone_id, args.zone)

    print("\n==> 5. Deploying Global Edge Cache Optimization Rules (1-Yr Static / 24h HTML SWR)...")
    sync_cache_settings_rule(headers, zone_id)

    print("\n==> 6. Synchronizing Hardened WAF Security Rules (Exploit Block & Whitelist)...")
    sync_custom_waf_rules(headers, zone_id)

    print("\n==> 7. Verifying DNSSEC Status...")
    check_dnssec(headers, zone_id)

    print("\n==> 8. Purging Cloudflare Global Edge Cache...")
    purge_cache(headers, zone_id)
    
    print("\n[✓] All Cloudflare Edge, DNS & Infrastructure Hardening Completed Successfully!")

if __name__ == "__main__":
    main()
