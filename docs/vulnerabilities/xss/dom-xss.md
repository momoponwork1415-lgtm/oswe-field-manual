# DOM XSS

## Common sources

Examples to recognize:

- `location.search`
- `location.hash`
- `location.href`
- `document.URL`
- `document.referrer`
- `postMessage`
- browser storage

A source is not automatically vulnerable. The important question is where the value flows.

## Common sinks

### HTML-parsing sinks

- `innerHTML`
- `outerHTML`
- `insertAdjacentHTML()`
- `document.write()`

### JavaScript execution sinks

- `eval()`
- `Function()`
- string arguments to `setTimeout()` / `setInterval()`

## Safer text-only operations

Depending on the intended behavior, APIs such as `textContent` or `innerText` avoid interpreting input as HTML.

## Analysis

```text
Source
  ↓
Transformation
  ↓
Sink
  ↓
Which parser/interpreter receives it?
  ↓
Can attacker-controlled data alter syntax?
```
