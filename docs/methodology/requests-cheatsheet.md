# Requests チートシート（Python PoC 用）

Web Security Academy の PoC を自分で書くときに参照する、HTTP 通信の最小メモ。例の URL と値は架空のもの。攻撃固有の payload や成功条件は、手動で確認した内容から決める。

## まず覚える形

```python
import requests

response = requests.get(
    "https://example.test/items",
    params={"q": "sample"},
    timeout=10,
)
print(response.status_code, response.url)
```

まずは `requests.get(...)` / `requests.post(...)` で 1 件の通信を再現する。複数の通信で Cookie を維持するときに `requests.Session()` を使う。`timeout` を省略すると待ち続ける場合がある。([Session](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects)・[Timeouts](https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts))

## どこへ値を入れるか

| HTTP 上の場所 | 書き方 | 例 |
| --- | --- | --- |
| URL のクエリ | `params=` | `requests.get(url, params={"q": value}, timeout=10)` |
| フォームの本文 | `data=` | `requests.post(url, data={"name": value}, timeout=10)` |
| JSON の本文 | `json=` | `requests.post(url, json={"name": value}, timeout=10)` |
| ヘッダー | `headers=` | `requests.get(url, headers={"X-Test": value}, timeout=10)` |
| 単発の Cookie | `cookies=` | `requests.get(url, cookies={"mode": value}, timeout=10)` |

`params` は URL のクエリを組み立てる。`data` に辞書を渡すと通常のフォーム形式になり、`json` は JSON へ変換して適切な Content-Type を付ける。**同じ名前のパラメータを複数送る**場合は `params=[("q", "a"), ("q", "b")]` や `data=[("q", "a"), ("q", "b")]` を使える。`json` と `data` / `files` を同時に渡すと `json` は無視される。([Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls)・[POST data](https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests))

## 応答と実際の送信内容

```python
response.status_code      # HTTP ステータス
response.url              # リダイレクト後の URL
response.headers          # 応答ヘッダー
response.text             # デコード後の本文（文字列）
response.content          # 本文の bytes
response.json()           # JSON を解析。JSON でなければ例外
response.cookies          # 応答で設定された Cookie
response.history          # リダイレクト履歴

response.request.method   # 最終リクエストのメソッド
response.request.url      # 最終リクエストの URL
response.request.headers  # 送信したヘッダー
response.request.body     # 送信した本文
```

`response.request.url` で **送信時の URL エンコード**を、`response.text` で **サーバーの応答**を別々に確認する。XSS の反射を確かめる際、応答に文字列が含まれた事実だけではブラウザでの JavaScript 実行は証明できない。リダイレクト前の応答を確認したい場合は `allow_redirects=False` を指定する。`response.json()` が成功しても HTTP の成功は意味しない。([Response content](https://requests.readthedocs.io/en/latest/user/quickstart/#response-content)・[Redirects](https://requests.readthedocs.io/en/latest/user/quickstart/#redirection-and-history))

## 失敗を見分ける

```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.Timeout:
    print("タイムアウト")
except requests.RequestException as exc:
    print(f"HTTP 通信エラー: {exc}")
```

`raise_for_status()` は 4xx / 5xx を例外にする。攻撃の判定に 4xx / 5xx が必要なら呼ぶ前に `status_code` を確認する。HTTP 200 だけで Exploit 成功とせず、目的に合うレスポンスや状態を確認する。`timeout=10` は処理全体の厳密な 10 秒制限ではない。([Status codes](https://requests.readthedocs.io/en/latest/user/quickstart/#response-status-codes)・[Errors](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions))

## 必要になったとき

```python
# プロキシ経由で Burp などへ送る
proxy = "http://127.0.0.1:8080"
response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=10)

# multipart/form-data でファイルを送る
with open("sample.txt", "rb") as file:
    response = requests.post(url, files={"file": file}, timeout=10)

# Basic 認証
response = requests.get(url, auth=("user", "password"), timeout=10)
```

HTTPS の証明書検証は既定で有効。ローカルの検証環境で証明書エラーが出たら、まず CA 証明書やプロキシ設定を確認する。`verify=False` は証明書検証を無効にするため、常用しない。([Proxies](https://requests.readthedocs.io/en/latest/user/advanced/#proxies)・[SSL Cert Verification](https://requests.readthedocs.io/en/latest/user/advanced/#ssl-cert-verification)・[Multipart](https://requests.readthedocs.io/en/latest/user/quickstart/#post-a-multipart-encoded-file))

## 自作 PoC での確認順

1. Burp / ブラウザで、メソッド・URL・パラメータの位置を確認する。
2. `params` / `data` / `json` のどれかを選び、まず普通の値で再現する。
3. `response.request` と `response` を見比べ、送信内容と応答を確認する。
4. 手動で確認した攻撃手順と成功条件を、自分の PoC に追加する。

詳しい API は [Requests Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)、[Advanced Usage](https://requests.readthedocs.io/en/latest/user/advanced/)、[Developer Interface](https://requests.readthedocs.io/en/latest/api/) を参照。
