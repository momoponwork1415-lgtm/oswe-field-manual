# DOM XSS

## よく見るSource

例:

- `location.search`
- `location.hash`
- `location.href`
- `document.URL`
- `document.referrer`
- `postMessage`
- Browser Storage

Sourceが存在するだけでは脆弱性ではありません。
**その値が最終的にどこへ流れるか**を確認します。

## よく見るSink

### HTMLを解釈するSink

- `innerHTML`
- `outerHTML`
- `insertAdjacentHTML()`
- `document.write()`

### JavaScriptを実行し得るSink

- `eval()`
- `Function()`
- 文字列を渡した `setTimeout()` / `setInterval()`

## テキスト出力用API

用途によっては、`textContent` や `innerText` のようなHTMLとして解釈しないAPIが安全側になります。

## 分析手順

```text
Source
  ↓
Transformation
  ↓
Sink
  ↓
どのParser / Interpreterが受け取るか
  ↓
攻撃者入力で構文を変えられるか
```
