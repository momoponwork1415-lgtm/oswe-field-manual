# XSS

## 基本の考え方

```text
Input
  ↓
Source
  ↓
Transformation / Encoding
  ↓
Sink
  ↓
Browser Parsing Context
  ↓
Execution
```

目的はpayloadを暗記することではありません。

**どのパーサーが入力を解釈しているか、実行可能なJavaScriptへ到達するために何を脱出・終了させる必要があるか**を考えます。

## 主なContext

- HTML Context
- HTML Attribute Context
- JavaScript Context
- URL Context
- DOM XSS
- Encoding / Decoding Boundary

## レビュー時の確認項目

- 攻撃者入力はどこから来るか
- 出力までにどんな変換が入るか
- 最終的にどのSinkへ入るか
- 次にどのパーサーが解釈するか
- どの文字がEncode / Filter / Decodeされるか
- どの構文やContextを脱出する必要があるか
