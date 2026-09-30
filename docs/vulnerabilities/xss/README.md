# XSS

## Mental model

```text
Input
  ↓
Source
  ↓
Transformation / Encoding
  ↓
Sink
  ↓
Browser parsing context
  ↓
Execution
```

The goal is not to memorize payloads. Determine which parser is active and what must be escaped or terminated to reach executable JavaScript.

## Main areas

- HTML context
- HTML attribute context
- JavaScript context
- URL context
- DOM XSS
- encoding / decoding boundaries

## Review questions

- Where does attacker-controlled data originate?
- What transformations occur before output?
- Which sink receives the value?
- Which parser interprets it next?
- What characters are encoded, filtered, or decoded?
- What must be escaped or closed?
