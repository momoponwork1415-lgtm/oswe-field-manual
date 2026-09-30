# XSS Encoding メモ

Encoding は、どの Parser Context に対して行われているかをセットで考えます。

```text
Input
  ↓
Encoding
  ↓
必要なら Decoding
  ↓
HTML Parser
  ↓
必要なら JavaScript / URL Parser
```

区別したいもの:

- HTML Entity Encoding
- HTML Attribute Encoding
- JavaScript String Escaping
- URL Encoding

一度 Encode されたから安全とは限りません。

後段で Decode されたり、別の Parser へ Context が切り替わったりすると、最終的な意味が変わることがあります。

具体例は、実際の Lab で遭遇したものだけ追加します。
