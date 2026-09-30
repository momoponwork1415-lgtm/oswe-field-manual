# DOM XSS

## よく見る Source

例:

- `location.search`
- `location.hash`
- `location.href`
- `document.URL`
- `document.referrer`
- `postMessage`
- Browser Storage

Source が存在するだけでは脆弱性ではありません。重要なのは、その値が最終的にどこへ流れるかです。

## よく見る Sink

### HTML を解釈する Sink

- `innerHTML`
- `outerHTML`
- `insertAdjacentHTML()`
- `document.write()`

### JavaScript を実行し得る Sink

- `eval()`
- `Function()`
- 文字列を渡した `setTimeout()` / `setInterval()`

## テキスト出力用 API

用途によっては、`textContent` や `innerText` のような HTML として解釈しない API が安全側になります。

## 分析手順

```text
Source
  ↓
Transformation
  ↓
Sink
  ↓
どの Parser / Interpreter が受け取るか
  ↓
攻撃者入力で構文を変えられるか
```
