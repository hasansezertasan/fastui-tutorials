# Masonite and FastUI (not implemented)

> **Status: not implemented.** This directory is a placeholder.
> Masonite cannot be installed on the Python versions this repository uses.

[Masonite](https://docs.masoniteproject.com/) is a full-stack Python web framework.
FastUI could in principle be served from it like from any other framework (see [Other web frameworks](../../docs/tutorial/08-other-frameworks.md)): return the component tree as JSON from `/api/`, and the HTML shell from a catch-all route.

## Why there is no example

- **Masonite fails to install on current Python.**
  The latest release, 4.20.4, pins `pendulum==2.1.2` (and `watchdog==4.0.0`).
  Pendulum 2.1.2 publishes no wheel for current Python versions, so it is built from source, and its build script imports `distutils`, which was removed from the standard library in Python 3.12 ([PEP 632](https://peps.python.org/pep-0632/)).
  `uv pip install masonite` on Python 3.14 stops with `Failed to build pendulum==2.1.2` and `ModuleNotFoundError: No module named 'distutils'`.
- This repository targets Python 3.11+ and develops on 3.14, so a Masonite example could not be installed or tested in CI.
- Masonite is also a full project framework, with its own project scaffolding, service providers and `craft` CLI.
  A single-file example like the others would not show how it is really used, and a faithful one would be much larger than the rest.

## Alternatives

For a full-stack framework, see [`with-django`](../with-django/), which runs as a single-file project.

## If you want to implement it

Contributions are welcome once Masonite supports current Python versions, for instance by moving to a Pendulum release that ships wheels.
Follow the pattern in [`with-django`](../with-django/), then replace this README with the usual "How to run" instructions.
