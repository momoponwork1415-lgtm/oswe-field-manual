# XSS Contexts

Keep this file small. Add examples only after encountering them in labs.

## HTML context

Attacker input becomes part of HTML text.

Think about:

- which HTML parser state receives the value,
- whether tags can be introduced,
- which characters are encoded.

## Attribute context

Input appears inside an HTML attribute.

Check:

- quoted vs unquoted attributes,
- quote character,
- whether a new attribute or element can be introduced,
- whether the attribute itself has executable behavior.

## JavaScript context

Input appears inside JavaScript source.

Check:

- string delimiter,
- escaping behavior,
- surrounding syntax,
- whether HTML encoding matters before the JS parser sees the value.

## URL context

Input appears in values such as `href`, `src`, or navigation APIs.

Understand both URL parsing and the eventual execution context.

## DOM context

Client-side JavaScript reads data from a source and sends it to a sink.

Trace the runtime data flow rather than only the server response.
