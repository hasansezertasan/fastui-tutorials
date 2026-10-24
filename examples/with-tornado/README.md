# Tornado and FastUI

> See [Other web frameworks](../../docs/tutorial/08-other-frameworks.md) in the tutorial for how the framework examples compare.

FastUI is not tied to FastAPI. This example serves a FastUI page from [Tornado](https://www.tornadoweb.org/), an async framework and networking library.

The recipe is the same for any framework:

1. **`/api/`** returns the component tree as JSON: `FastUI(root=[c.Heading(text="Hello World")])`.
2. **A catch-all route, registered last,** returns `prebuilt_html(...)`, the HTML shell that loads the FastUI React app.
   The React app then fetches `/api/<same path>` to learn what to render.

## What is specific to Tornado

Handlers are matched in list order, so `/api/` is listed before the `/(.*)` catch-all.

Used Components:

- `Heading`

## How to run

### Clone the repo

```shell
git clone https://github.com/hasansezertasan/fastui-tutorials.git
cd fastui-tutorials
```

### Change directory to the example

```shell
cd examples/with-tornado
```

### Run the application

```shell
uv run with-tornado
```

Then open `http://127.0.0.1:8000`.

### Run the tests

```shell
uv run pytest
```
