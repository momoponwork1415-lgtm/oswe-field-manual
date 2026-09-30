# XSS Encoding Notes

Encoding only makes sense relative to a parser context.

Track the complete sequence:

```text
Input
  ↓
Encoding
  ↓
Possible decoding
  ↓
HTML parser
  ↓
Possible JavaScript / URL parser
```

Areas to distinguish:

- HTML entity encoding
- HTML attribute encoding
- JavaScript string escaping
- URL encoding

Do not assume that because a character is encoded once it remains harmless. A later decoding or parser transition may change the effective value.

Add concrete examples here only after encountering them during study.
