# Emmett and FastUI

> See [Other web frameworks](../../docs/tutorial/08-other-frameworks.md) in the tutorial for how the framework examples compare.

FastUI is not tied to FastAPI. This example serves a FastUI page from [Emmett](https://emmett.sh/), an async full-stack framework served by Granian.

The recipe is the same for any framework:

1. **`/api/`** returns the component tree as JSON: `FastUI(root=[c.Heading(text="Hello World")])`.
2. **A catch-all route, registered last,** returns `prebuilt_html(...)`, the HTML shell that loads the FastUI React app.
   The React app then fetches `/api/<same path>` to learn what to render.

FastUI itself still needs FastAPI installed, because it imports `fastapi` at load time. That is why the dependency is `fastui[fastapi]`.

## What is specific to Emmett

Emmett strips trailing slashes before routing, so the API route is registered as `/api` and still serves `/api/`.

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
cd examples/with-emmett
```

### Run the application

```shell
uv run with-emmett
```

Then open `http://127.0.0.1:8000`.

### Run the tests

```shell
uv run pytest
```
