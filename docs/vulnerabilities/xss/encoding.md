# XSS Encoding メモ

Encodingは、**どのParser Contextに対して行われているか**をセットで考えます。

処理全体を追います。

```text
Input
  ↓
Encoding
  ↓
必要ならDecoding
  ↓
HTML Parser
  ↓
必要ならJavaScript / URL Parser
```

区別したいもの:

- HTML Entity Encoding
- HTML Attribute Encoding
- JavaScript String Escaping
- URL Encoding

一度Encodeされたから安全とは限りません。

後段でDecodeされたり、別のParserへContextが切り替わったりすると、最終的な意味が変わることがあります。

具体例は、実際のLabで遭遇したものだけ追加します。
