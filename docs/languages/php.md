# セキュリティコードリーディング用 PHP メモ

一般的な PHP 入門ではなく、Web アプリケーションのセキュリティレビュー中に重要だった構文・API だけを記録します。

## 攻撃者が制御しやすい HTTP 入力

代表例:

- `$_GET`
- `$_POST`
- `$_REQUEST`
- `$_COOKIE`
- `$_FILES`
- 一部の HTTP Header を含む `$_SERVER`

## セッション

- `$_SESSION`

Session 値だから常に安全とは限りません。

その Session 値がどのように生成・更新されたかによっては、攻撃者が間接的に制御できる場合があります。

## コードを読むときの基本

各値について次の流れを追います。

```text
Request / Session Source
  ↓
Validation
  ↓
Transformation
  ↓
Business Logic
  ↓
Sink
```

フレームワーク固有の構文や API は、Lab や WEB-300 で実際に遭遇したものだけ追加します。
