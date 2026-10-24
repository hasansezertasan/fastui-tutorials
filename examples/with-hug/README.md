# Hug and FastUI (not implemented)

> **Status: not implemented.** This directory is a placeholder.
> It cannot run on the Python versions this repository supports.

[Hug](https://github.com/hugapi/hug) is a Python API framework.
FastUI could in principle be served from it like from any other framework (see [Other web frameworks](../../docs/tutorial/08-other-frameworks.md)): return the component tree as JSON from `/api/`, and the HTML shell from a catch-all route.

## Why there is no example

- **Hug does not import on Python 3.13 and later.**
  The latest release, 2.6.1, is from February 2020 and pins Falcon 2.0.0.
  Falcon 2.0.0 vendors `mimeparse`, which does `import cgi`.
  The `cgi` module was removed from the standard library in Python 3.13 ([PEP 594](https://peps.python.org/pep-0594/)), so `import hug` fails with `ModuleNotFoundError: No module named 'cgi'`.
- **Hug is unmaintained.** There has been no release since 2020, so the problem will not be fixed upstream.
- This repository targets Python 3.11+ and develops on 3.14, so a Hug example could not be run or tested in CI.

Hug might work on Python 3.11 or 3.12. That has not been tested, and an example that only works on old Python versions would not be a useful tutorial.

## Alternatives

Falcon, the framework Hug is built on, has a working example: [`with-falcon`](../with-falcon/).

## If you want to implement it

Contributions are welcome if Hug gains support for current Python versions.
Follow the pattern in [`with-falcon`](../with-falcon/), then replace this README with the usual "How to run" instructions.
