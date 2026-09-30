# OSWE Field Manual

A study repository for building practical OSWE / WEB-300 skills through hands-on labs, code reading, and exploit development.

## Goal

Build the ability to take an unfamiliar web application and:

1. understand its framework and request flow,
2. trace attacker-controlled input,
3. identify vulnerable behavior,
4. turn the behavior into an exploitable primitive,
5. chain primitives when necessary,
6. reproduce the result with a Python PoC.

## Study loop

```text
Learn / Read
    ↓
Web Security Academy or code-reading exercise
    ↓
Analyze without AI giving the lab answer
    ↓
Manual exploit
    ↓
Python PoC
    ↓
Extract reusable knowledge
    ↓
Update this repository
```

This repository is intentionally **not** a complete encyclopedia prepared in advance.
It should grow from problems actually encountered while studying.

## Structure

```text
docs/
  methodology/          White-box review workflow
  vulnerabilities/      Reusable vulnerability knowledge
  languages/            Security-oriented language/framework notes

web-security-academy/   Per-lab notes and Python PoCs
snippets/               Reusable small building blocks
boilerplates/           Generic exploit skeletons
```

## AI rule

AI may help organize references, explain concepts after solving, review code, and improve reusable notes.

For a first attempt at a lab or exercise, AI should not directly provide the vulnerability, payload, or final exploit.

## Current focus

1. XSS
2. SQL Injection
3. Command Injection
4. File Upload
5. Path Traversal
6. SSRF
7. XXE
8. SSTI
9. CSRF / JWT / Authentication

Then move into WEB-300 modules and white-box challenge labs.
