# Python PoC の書き方

## 現在の進め方: Web Security Academy

1. Lab を手動で解き、HTTP リクエストと応答を確認する。
2. 最初の Python PoC は [Requests チートシート](requests-cheatsheet.md)を参照して自分で書く。
3. 次の Lab では自作の過去ファイルをコピーし、Lab 名・攻撃手順・HTTP 通信・確認処理を書き替える。
4. 1 Lab につき 1 Python ファイルを保存する。冒頭コメントは Lab 名、手順、実行方法だけでよい。

関数名やファイルの骨格を固定しません。`Session`、CLI 引数、例外処理は Lab で必要になったところから使い、`requests` の挙動を理解することを優先します。HTTP 200 やペイロードの送信だけで成功とせず、今回の目的に合う応答を確認します。

## 参照先

PoC の作例は [rizemon/exploit-writing-for-oswe](https://github.com/rizemon/exploit-writing-for-oswe) を主に参照します。まず `Code Snippets` の Requests 部分と `Troubleshooting` を使い、実際に送ったリクエストと応答を観察します。API の正確な動作は [Requests 公式資料](https://requests.readthedocs.io/en/latest/user/quickstart/)で確認します。OSWE 試験の提出条件は [OffSec 公式ガイド](https://help.offsec.com/hc/en-us/articles/360046869951-WEB-300-Advanced-Web-Attacks-and-Exploitation-OSWE-Exam-Guide)を優先します。

この参考リポジトリは速度を重視した個人のノートで、コード例をそのまま規約にはしません。たとえば `Starting Template` の `__main__` に引用符がなく、`assert` による必須の成功判定は Python の `-O` 実行時に無効になります。([参考リポジトリ](https://github.com/rizemon/exploit-writing-for-oswe)・[Python の `assert`](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement))

## HTTP 通信の基本

### ライブラリの使い分け

- [`argparse`](https://docs.python.org/3/library/argparse.html) はコマンドライン引数を読むための標準ライブラリで、`parser` は通常その `ArgumentParser` オブジェクトを指す。
- [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html) はURLの分解・結合・エンコードが必要なときに使う。
- HTTP通信には `requests` を使う。標準ライブラリの [`urllib.request`](https://docs.python.org/3/library/urllib.request.html) もHTTP通信ができるが、Python公式ドキュメントは高水準のHTTPクライアントとしてRequestsを案内している。

### Requests の扱い

- 複数リクエストで Cookie や認証状態を維持するときは `requests.Session()` を使う。単発リクエストで必須ではない。([Requests: Session Objects](https://requests.readthedocs.io/en/stable/user/advanced/#session-objects))
- 各リクエストに `timeout` を指定する。Requests は省略時にタイムアウトしない。([Requests: Timeouts](https://requests.readthedocs.io/en/stable/user/advanced/#timeouts))
- クエリ、フォーム、JSON は `params`、`data`、`json` で渡す。URL文字列を手で連結する前に、実際のHTTPリクエストを確認する。([Requests: Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/))
- 期待しないHTTPエラーは `raise_for_status()` などで検出する。4xx/5xxが攻撃の証拠になる場合は、その意味を明示して判定する。([Requests: Response Status Codes](https://requests.readthedocs.io/en/latest/user/quickstart/#response-status-codes))
- `except:` で全例外を握りつぶさない。通信エラーと攻撃失敗を区別し、プログラムのバグは見えるようにする。

## 再利用する単位

まずは過去の自作 PoC をコピーして使います。認証、CSRF token 抽出、アップロードなど、実際に何度も書いた処理だけを後から [`snippets/`](../../snippets/) に保存します。各 PoC は単独で動く状態にし、Lab を初期状態に戻して再実行できるか確認します。

`requests` だけで確認できる範囲も明記します。たとえば XSS の応答への反射は確認できますが、JavaScript の実行そのものは確認できません。

## 後で: OSWE 形式の練習

WEB-300 の複数段階の課題に進むとき、[OffSec の OSWE Exam Guide](https://help.offsec.com/hc/en-us/articles/360046869951-WEB-300-Advanced-Web-Attacks-and-Exploitation-OSWE-Exam-Guide) が求める攻撃の連結と無対話の実行を確認します。現時点の単一 Lab では、[汎用雛形](../../boilerplates/exploit.py)へ合わせる必要はありません。
