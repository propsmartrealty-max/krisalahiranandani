#!/usr/bin/env python3
import re
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DEV = os.path.join(PROJECT_DIR, "app.dev.js")
APP_JS = os.path.join(PROJECT_DIR, "app.js")
APP_MIN = os.path.join(PROJECT_DIR, "app.min.js")
STYLE_DEV = os.path.join(PROJECT_DIR, "style.dev.css")
STYLE_CSS = os.path.join(PROJECT_DIR, "style.css")
STYLE_MIN = os.path.join(PROJECT_DIR, "style.min.css")

def minify_css(css):
    # Remove CSS comments
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    # Collapse multiple whitespace
    css = re.sub(r'\s+', ' ', css)
    # Remove whitespace around symbols
    css = re.sub(r'\s*([\{\}\:\;\,\>\+\~])\s*', r'\1', css)
    # Remove trailing semicolons before closing braces
    css = re.sub(r';\}', '}', css)
    return css.strip()

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

# Process JS
with open(APP_DEV, "r", encoding="utf-8") as f:
    js_src = f.read()

js_min = minify_js(js_src)
print(f"app.dev.js: {len(js_src)} bytes -> Minified: {len(js_min)} bytes")

with open(APP_JS, "w", encoding="utf-8") as f:
    f.write(js_min)

with open(APP_MIN, "w", encoding="utf-8") as f:
    f.write(js_min)

# Process CSS
with open(STYLE_DEV, "r", encoding="utf-8") as f:
    css_src = f.read()

css_min = minify_css(css_src)
print(f"style.dev.css: {len(css_src)} bytes -> Minified: {len(css_min)} bytes")

with open(STYLE_CSS, "w", encoding="utf-8") as f:
    f.write(css_min)

with open(STYLE_MIN, "w", encoding="utf-8") as f:
    f.write(css_min)

print("Saved all minified JS and CSS assets successfully!")
