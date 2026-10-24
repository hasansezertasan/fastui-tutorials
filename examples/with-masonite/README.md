# Masonite and FastUI (not implemented)

> **Status: not implemented.** This directory is a placeholder.
> Masonite is a project framework, so it does not fit the single-file style of the other examples.

[Masonite](https://docs.masonite.dev/) is a full-stack Python web framework.
FastUI could in principle be served from it like from any other framework (see [Other web frameworks](../../docs/tutorial/08-other-frameworks.md)): return the component tree as JSON from `/api/`, and the HTML shell from a catch-all route.

## Why there is no example

- **Masonite is built around a generated project, not a module.**
  A Masonite app boots from a top-level `wsgi.py` that defines `application`, and the framework's facades (`config(...)`, `Response`, and so on) do `from wsgi import application` internally.
  Its configuration is loaded from a `config/` directory of files (`application.py`, `providers.py`, `security.py`, ...), and routes, controllers and middleware live in their own directories.
- **A single-file example was tried and does not work.**
  Booting the framework with `CoreKernel` and a handful of providers fails without a real `config/` directory under the working directory, and the `wsgi` module has to exist by name.
  Working around that means faking a project layout inside the package, which would teach readers the wrong way to use Masonite.
- **A faithful example would be a generated project** (`craft new`, then dozens of files), which is a different shape from the one-package examples in this repository, and much larger than the rest.

## Which package to use

Masonite 5 is published on PyPI as **`masonite-framework`**.
The old `masonite` package (4.x and earlier, the last release being 4.20.4) is deprecated.
It pins `pendulum==2.1.2`, whose build needs `distutils`, so `pip install masonite` fails on current Python.
`masonite-framework` installs and imports on Python 3.13 and 3.14, so that is not what blocks an example here.

## Alternatives

For a full-stack framework, see [`with-django`](../with-django/), which runs as a single-file project.

## If you want to implement it

Contributions are welcome.
The honest shape is a small generated Masonite 5 project with `masonite-framework` and `fastui[fastapi]` as dependencies, an `/api/` route that returns the component tree, and a catch-all route that returns `prebuilt_html(...)`.
If you do that, replace this README with the usual "How to run" instructions.
