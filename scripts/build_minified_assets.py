#!/usr/bin/env python3
import re
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DEV = os.path.join(PROJECT_DIR, "app.dev.js")
APP_JS = os.path.join(PROJECT_DIR, "app.js")
APP_MIN = os.path.join(PROJECT_DIR, "app.min.js")

with open(APP_DEV, "r", encoding="utf-8") as f:
    src = f.read()

def minify_js(source):
    result = []
    i = 0
    n = len(source)
    while i < n:
        if source[i:i+2] == '//':
            end = source.find('\n', i)
            if end == -1:
                break
            i = end + 1
        elif source[i:i+2] == '/*':
            end = source.find('*/', i)
            if end == -1:
                break
            i = end + 2
        elif source[i] in ('"', "'", '`'):
            quote = source[i]
            result.append(quote)
            i += 1
            while i < n:
                char = source[i]
                result.append(char)
                if char == '\\':
                    i += 1
                    if i < n:
                        result.append(source[i])
                elif char == quote:
                    i += 1
                    break
                i += 1
        else:
            result.append(source[i])
            i += 1
    
    code = ''.join(result)
    lines = [l.strip() for l in code.split('\n') if l.strip()]
    return '\n'.join(lines)

minified = minify_js(src)
print(f"app.dev.js: {len(src)} bytes -> Minified: {len(minified)} bytes")

with open(APP_JS, "w", encoding="utf-8") as f:
    f.write(minified)

with open(APP_MIN, "w", encoding="utf-8") as f:
    f.write(minified)

print("Saved app.js and app.min.js successfully!")
