# Python PoC の書き方

## 公式要件とこのリポジトリの方針

OffSec の [OSWE Exam Guide](https://help.offsec.com/hc/en-us/articles/360046869951-WEB-300-Advanced-Web-Attacks-and-Exploitation-OSWE-Exam-Guide) は、試験対象ごとに複数の脆弱性を利用する機能的なスクリプトを1本用意し、実行中に採点者の手作業を必要としないことを求めています。リバースシェルを得ない場合は proof 値の自動取得も必要です。PoC のソースコードは試験レポートの PDF 内に含めます。関数名、コメントの書式、Python の雛形は指定していません。

以下は学習用のローカル規約です。Web Security Academy では1 Labにつき1つの Python ファイルを書き、本番形式の練習では攻撃経路を対象ごとに1本へまとめます。

## ファイルの骨格

1. 冒頭コメントに対象、目的、攻撃手順、前提条件、実行方法、成功の証拠を書く。
2. `parse_args()` で対象URLと必要な設定を受け取る。コールバックを使う場合はリスナーのアドレスとポートも指定できるようにする。実行中の `input()` は使わない。
3. 攻撃経路を `exploit()` に書く。複数段階なら、各段階を短い関数に分けて呼び出す。
4. `verify()` で目的に合う証拠を確認する。HTTP 200 やペイロードの送信だけで成功としない。
5. `main()` で Session、エラー、終了コードを管理する。成功時は証拠を表示して0、失敗時は理由を表示して非0を返す。

[汎用雛形](../../boilerplates/exploit.py)はこの骨格だけを提供します。実際の攻撃と成功条件は、自分で手動再現した結果から埋めます。

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

認証、CSRF token 抽出、アップロード、blind extraction など、複数のLabで繰り返した短い処理だけを [`snippets/`](../../snippets/) に保存します。各PoCは必要な処理を取り込み、単独で動く状態にします。Labを初期状態に戻して再実行し、ヘッダーに書いた成功の証拠が得られるか確認します。

`requests` だけで確認できる範囲も明記します。たとえば XSS の応答への反射は確認できますが、JavaScript の実行そのものは確認できません。
