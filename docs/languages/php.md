# PHP for Security Code Reading

This is not a general PHP tutorial. Record PHP constructs that matter while reviewing web applications.

## Attacker-controlled request data

Common sources:

- `$_GET`
- `$_POST`
- `$_REQUEST`
- `$_COOKIE`
- `$_FILES`
- selected server headers through `$_SERVER`

## State

- `$_SESSION`

Session values may be trusted or attacker-influenced depending on how they were created.

## Review habit

For each value, trace:

```text
request/session source
  ↓
validation
  ↓
transformation
  ↓
business logic
  ↓
sink
```

Add framework-specific syntax and APIs only when they appear in labs or WEB-300.
