# セキュリティコードリーディング用 PHP メモ

一般的なPHP入門ではなく、Webアプリケーションのセキュリティレビュー中に重要だった構文・APIだけを記録します。

## 攻撃者が制御しやすいHTTP入力

代表例:

- `$_GET`
- `$_POST`
- `$_REQUEST`
- `$_COOKIE`
- `$_FILES`
- 一部のHTTP Headerを含む `$_SERVER`

## セッション

- `$_SESSION`

Session値だから常に安全とは限りません。

そのSession値が**どのように生成・更新されたか**によっては、攻撃者が間接的に制御できる場合があります。

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

フレームワーク固有の構文やAPIは、LabやWEB-300で実際に遭遇したものだけ追加します。
