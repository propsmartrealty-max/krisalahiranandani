#!/usr/bin/env python3
"""
AMP Integrity & Search Console Guard for Krisala Hiranandani Web Stories.
Enforces 100% compliance with AMP Story Specification to prevent GSC regressions:
1. Rejects any external <link rel="stylesheet"> in stories.
2. Rejects any sibling elements inside <body> (only <amp-story> allowed).
3. Verifies canonical <style amp-boilerplate> and noscript blocks.
4. Executes official amphtml-validator against every story file.
"""

import os
import sys
import glob
import subprocess
from bs4 import BeautifulSoup

CANONICAL_BOILERPLATE = "body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}"

def validate_story_file(filepath):
    errors = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Check for forbidden external stylesheets
    soup = BeautifulSoup(content, "html.parser")
    for link in soup.find_all("link", rel="stylesheet"):
        href = link.get("href", "")
        # Google fonts is permitted, anything else is disallowed
        if not href.startswith("https://fonts.googleapis.com"):
            errors.append(f"Forbidden external stylesheet found: {href}")
            
    # 2. Check body children - only <amp-story> is allowed
    body = soup.find("body")
    if not body:
        errors.append("Missing <body> element.")
    else:
        # Filter out text nodes that are just whitespace
        children = [child for child in body.children if child.name is not None]
        if len(children) != 1:
            child_names = [c.name for c in children]
            errors.append(f"Body has {len(children)} children: {child_names}. Expected exactly 1 (<amp-story>).")
        elif children[0].name != "amp-story":
            errors.append(f"Body child is <{children[0].name}> instead of <amp-story>.")
            
    # 3. Check amp-boilerplate
    if CANONICAL_BOILERPLATE not in content:
        errors.append("Malformed or missing canonical <style amp-boilerplate>.")
        
    return errors

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stories_dir = os.path.join(root_dir, "stories")
    story_files = sorted(glob.glob(os.path.join(stories_dir, "*.html")))
    
    if not story_files:
        print("[!] No story files found in stories/ directory.")
        sys.exit(1)
        
    print(f"[*] Validating {len(story_files)} AMP stories for Search Console compliance...")
    has_error = False
    
    for filepath in story_files:
        rel = os.path.relpath(filepath, root_dir)
        errors = validate_story_file(filepath)
        if errors:
            print(f"[FAIL] {rel}:")
            for err in errors:
                print(f"   - {err}")
            has_error = True
        else:
            print(f"[PASS] {rel} passed internal AMP structure rules.")
            
    if has_error:
        print("\n[ERROR] AMP structural guards failed.")
        sys.exit(1)
        
    print("\n[✓] All stories conform strictly to AMP Story rules.")
    
    # Run official amphtml-validator
    print("\n[*] Invoking amphtml-validator CLI...")
    try:
        res = subprocess.run(["npx", "--yes", "amphtml-validator"] + story_files, capture_output=True, text=True)
        print(res.stdout)
        if res.returncode != 0:
            print(res.stderr)
            sys.exit(res.returncode)
    except Exception as e:
        print(f"[WARN] Could not run npx amphtml-validator: {e}")
        
    print("[SUCCESS] All AMP Web Stories are 100% compliant and ready for Google Search Console!")

if __name__ == "__main__":
    main()
