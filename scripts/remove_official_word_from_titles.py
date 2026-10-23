#!/usr/bin/env python3
"""
Remove ONLY the word 'Official' from all titles across the Krisala Hiranandani website.
Preserves all brand keywords, trademarks ™, price anchors, and structural formatting.
"""

import os
import glob
import re
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def clean_official_from_title(title):
    if not title:
        return title
    t = title
    # Remove 【Official】 bracket completely
    t = re.sub(r'【Official】\s*', '', t)
    # If bracket has other words e.g. 【Official Comparison】 -> 【Comparison】
    t = re.sub(r'【Official\s+', '【', t)
    # Remove standalone word Official
    t = re.sub(r'\bOfficial\b\s*', '', t, flags=re.IGNORECASE)
    # Clean up any duplicate spaces or leading/trailing dashes/colons/pipes
    t = re.sub(r'\s+', ' ', t).strip(' -|')
    return t

def process_html_files():
    all_html_files = sorted(glob.glob(os.path.join(ROOT_DIR, "**", "*.html"), recursive=True))
    modified_count = 0
    
    for file_path in all_html_files:
        if "node_modules" in file_path or ".git" in file_path:
            continue
            
        rel_path = os.path.relpath(file_path, ROOT_DIR)
        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()
            
        soup = BeautifulSoup(html, "html.parser")
        modified = False
        
        if soup.title and soup.title.string:
            old_title = soup.title.string.strip()
            if "official" in old_title.lower():
                new_title = clean_official_from_title(old_title)
                soup.title.string = new_title
                
                # Update og:title
                og_t = soup.find("meta", property="og:title")
                if og_t and og_t.get("content"):
                    og_t["content"] = clean_official_from_title(og_t["content"])
                elif og_t:
                    og_t["content"] = new_title
                    
                # Update twitter:title
                tw_t = soup.find("meta", attrs={"name": "twitter:title"})
                if tw_t and tw_t.get("content"):
                    tw_t["content"] = clean_official_from_title(tw_t["content"])
                elif tw_t:
                    tw_t["content"] = new_title
                    
                modified = True
                modified_count += 1
                print(f"[{rel_path}]\n  BEFORE: {old_title}\n  AFTER:  {new_title}\n")
                
        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(str(soup))
                
    print(f"=== Total HTML Pages Updated: {modified_count} ===")

def process_edge_worker():
    worker_path = os.path.join(ROOT_DIR, "functions", "explore", "[[slug]].js")
    if os.path.exists(worker_path):
        with open(worker_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace 【Official】 in metaTitle assignments
        new_content = re.sub(r'【Official】\s*', '', content)
        new_content = re.sub(r'【Official\s+', '【', new_content)
        new_content = re.sub(r'Official\s+Hiranandani\s+Pune\s+Project', 'Hiranandani Pune Project', new_content)
        
        if new_content != content:
            with open(worker_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("Updated functions/explore/[[slug]].js to remove 'Official' from dynamic metaTitle generation.")

if __name__ == "__main__":
    process_html_files()
    process_edge_worker()
