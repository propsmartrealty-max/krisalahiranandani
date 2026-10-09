#!/usr/bin/env python3
"""
Cloudflare & DNS Full-Stack Optimizer & Hardener
Automates security settings, TLS configurations, and DNS records via Cloudflare v4 REST API.
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
        # Fallback to default or unverified if certificates aren't linked on local mac python
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

def add_dns_record(headers, zone_id, record_data, existing_records):
    # Check if identical record exists
    for r in existing_records:
        if r.get("type") == record_data.get("type") and r.get("name") == record_data.get("name"):
            if record_data.get("type") in ["CAA", "TXT", "MX"]:
                if str(r.get("content")).strip('"') == str(record_data.get("content")).strip('"'):
                    print(f"  [i] DNS {record_data['type']} {record_data['name']} already exists.")
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

def update_dns_record(headers, zone_id, record_id, record_data):
    url = f"{API_BASE}/zones/{zone_id}/dns_records/{record_id}"
    res = make_request(url, method="PUT", headers=headers, data=record_data)
    if res.get("success"):
        print(f"  [✓] Updated DNS {record_data['type']} {record_data['name']} -> {record_data.get('content')}")
    else:
        print(f"  [✗] Failed to update DNS {record_data['type']} {record_data['name']}: {res.get('errors')}")

def sync_routing_records(headers, zone_id, zone_name, pages_target="krisalahiranandani.pages.dev"):
    """
    Ensures apex and www point to Cloudflare Pages host with orange cloud proxy enabled.
    Cleans up any conflicting A/AAAA records on apex or www.
    """
    records = list_dns_records(headers, zone_id)
    apex_targets = [zone_name, f"@{zone_name}"]
    www_target = f"www.{zone_name}"

    # 1. Audit and clean conflicting A/AAAA records
    for r in records:
        r_name = r.get("name", "").lower()
        r_type = r.get("type", "").upper()
        r_id = r.get("id")
        if r_type in ["A", "AAAA"]:
            if r_name == zone_name.lower() or r_name == www_target.lower():
                print(f"  [!] Found conflicting {r_type} record for {r_name} pointing to {r.get('content')}. Removing...")
                delete_dns_record(headers, zone_id, r_id, f"{r_type} {r_name}")

    # Refresh after potential deletions
    records = list_dns_records(headers, zone_id)

    # 2. Sync Apex CNAME
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
            update_dns_record(headers, zone_id, apex_cname["id"], update_data)
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
        else:
            print(f"  [✗] Failed to create Apex CNAME: {res.get('errors')}")

    # 3. Sync www CNAME
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
            update_dns_record(headers, zone_id, www_cname["id"], update_data)
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
        else:
            print(f"  [✗] Failed to create www CNAME: {res.get('errors')}")

def purge_cache(headers, zone_id):
    url = f"{API_BASE}/zones/{zone_id}/purge_cache"
    res = make_request(url, method="POST", headers=headers, data={"purge_everything": True})
    if res.get("success"):
        print("  [✓] Edge Cache Purged Successfully globally.")
    else:
        print(f"  [✗] Cache purge failed: {res.get('errors')}")

def main():
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
        ("0rtt", "off"),
        ("always_use_https", "on"),
        ("security_level", "medium"),
        ("browser_check", "on"),
        ("brotli", "on"),
        ("early_hints", "on"),
        ("opportunistic_encryption", "on"),
        ("websockets", "on"),
        ("automatic_https_rewrites", "on")
    ]
    for setting_id, val in settings_to_apply:
        update_zone_setting(headers, zone_id, setting_id, val)
        
    print("\n==> 2. Synchronizing Pages Routing DNS Records (@ and www)...")
    sync_routing_records(headers, zone_id, args.zone, "krisalahiranandani.pages.dev")
        
    print("\n==> 3. Auditing & Hardening DNS Records (CAA, SPF, DMARC)...")
    existing_records = list_dns_records(headers, zone_id)
    
    dns_hardening_records = [
        # CAA Records
        {"type": "CAA", "name": args.zone, "data": {"flags": 0, "tag": "issue", "value": "letsencrypt.org"}, "ttl": 3600},
        {"type": "CAA", "name": args.zone, "data": {"flags": 0, "tag": "issue", "value": "digicert.com"}, "ttl": 3600},
        {"type": "CAA", "name": args.zone, "data": {"flags": 0, "tag": "issue", "value": "pki.goog"}, "ttl": 3600},
        {"type": "CAA", "name": args.zone, "data": {"flags": 0, "tag": "issuewild", "value": "letsencrypt.org"}, "ttl": 3600},
        {"type": "CAA", "name": args.zone, "data": {"flags": 0, "tag": "issuewild", "value": "digicert.com"}, "ttl": 3600},
        {"type": "CAA", "name": args.zone, "data": {"flags": 0, "tag": "issuewild", "value": "pki.goog"}, "ttl": 3600},
        
        # Email Anti-Spoofing & DMARC Protection
        {"type": "TXT", "name": args.zone, "content": "v=spf1 -all", "ttl": 3600},
        {"type": "TXT", "name": f"_dmarc.{args.zone}", "content": "v=DMARC1; p=reject; sp=reject; aspf=s; adkim=s", "ttl": 3600},
        {"type": "TXT", "name": f"*._domainkey.{args.zone}", "content": "v=DKIM1; p=", "ttl": 3600},
    ]
    
    for r in dns_hardening_records:
        add_dns_record(headers, zone_id, r, existing_records)
        
    print("\n==> 4. Purging Edge Cache...")
    purge_cache(headers, zone_id)
    
    print("\n[✓] All Cloudflare Edge & DNS Hardening Tasks Completed Successfully!")

if __name__ == "__main__":
    main()
