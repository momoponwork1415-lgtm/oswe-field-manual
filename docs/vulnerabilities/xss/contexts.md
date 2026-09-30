# XSS Context

このファイルは小さく保ちます。実際のLabで遭遇した例だけを追加します。

## HTML Context

攻撃者入力がHTML本文の一部として出力されるケースです。

確認すること:

- HTML Parser のどの状態で入力されるか
- 新しいHTMLタグを作れるか
- どの文字がEncodeされるか

## Attribute Context

入力がHTML属性値の中に入るケースです。

確認すること:

- Quoted / Unquoted のどちらか
- 使用されている引用符
- 属性値を閉じて新しい属性やタグを追加できるか
- その属性自体に実行可能な意味があるか

## JavaScript Context

入力がJavaScriptソースコードの中に入るケースです。

確認すること:

- 文字列Delimiter
- Escape処理
- 周囲のJavaScript構文
- JavaScript Parser に届く前にHTML Encodingが入るか

## URL Context

`href`、`src`、Navigation API などURLとして扱われる場所に入力が入るケースです。

URL Parser と、その後に入力を処理するContextの両方を確認します。

## DOM Context

クライアント側JavaScriptがSourceから値を取得し、Sinkへ渡すケースです。

サーバーレスポンスだけを見るのではなく、ブラウザ実行時のデータフローを追います。
