# White-box Workflow

Use this as the default review loop for unfamiliar web applications.

## 1. Understand normal behavior

- What feature is being used?
- What request reaches it?
- What authentication state is required?
- What changes in the response or server state?

## 2. Map the application

Trace:

```text
Route
  ↓
Controller / Handler
  ↓
Request data
  ↓
Validation / Transformation
  ↓
Business logic
  ↓
DB / Template / File / HTTP / Command / Deserialization
```

## 3. Trace data in both directions

### Source → Sink

Start from attacker-controlled input and follow it forward.

### Sink → Source

Start from dangerous operations and determine whether attacker-controlled data can reach them.

Do not stop at obvious sinks. Also inspect authentication, authorization, state transitions, and business logic.

## 4. Identify the primitive

Do not only name the vulnerability. Ask:

> What new capability does the attacker gain?

Examples:

- read arbitrary DB data
- send server-side HTTP requests
- read files
- write files
- execute template expressions
- act as another user
- reach an internal-only feature

## 5. Exploit

Understand constraints, build the exploit manually, then automate it.

## 6. Reproduce

Reset/revert the target and confirm the exploit from a clean state with a single PoC.
