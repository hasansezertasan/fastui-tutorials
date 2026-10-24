# 8. Other web frameworks

Examples: the `examples/with-*` projects.

Nothing in [chapter 1](01-how-fastui-works.md) requires FastAPI *to serve* a FastUI app.
FastUI is a set of Pydantic models plus a prebuilt React app, so any framework that can return JSON and HTML can serve it.

One catch: the `fastui` package imports `fastapi` when it loads, because its form helpers use it.
So even a Flask or Django app must install FastAPI alongside, which is what the `fastui[fastapi]` dependency in each example's `pyproject.toml` does. Plain `fastui` fails with `ImportError: fastui.dev requires fastapi to be installed`.

The recipe is always:

1. Serve `/api/...` routes that return `FastUI(root=[...]).model_dump_json(by_alias=True, exclude_none=True)` with a JSON content type.
   `by_alias=True` matters: FastUI's React app reads camelCase keys such as `onClick` and `className`, while Pydantic emits `on_click` and `class_name` unless asked to use the aliases. FastAPI's `response_model` does this for you, but when you serialize by hand you must. A bare `Heading` hides the mistake, so it only shows once a component has an event or a class.
2. Serve a catch-all route that returns `prebuilt_html(title=...)` as HTML, registered so it does not shadow `/api/`.

Compare how little changes:

```python
# Flask
@app.get("/api/")
def page() -> Response:
    return jsonify(FastUI(root=[c.Heading(text="Hello World")]).model_dump(by_alias=True, exclude_none=True))

# Starlette
def page(request: Request) -> JSONResponse:
    return JSONResponse(FastUI(root=[c.Heading(text="Hello World")]).model_dump(by_alias=True, exclude_none=True))
```

You lose FastAPI's `response_model` and `fastui_form` helpers, and a framework's own routing quirks matter.
Most of the differences between the examples are about **route ordering**, because the catch-all must not swallow `/api/`.

| Framework | Style | Gotcha |
| --- | --- | --- |
| [Starlette](../../examples/with-starlette/) | ASGI | Routes match in list order |
| [Litestar](../../examples/with-litestar/) | ASGI | Static routes win over the `/{path:path}` catch-all. Serializes the model itself, so enable `PydanticPlugin(prefer_alias=True, exclude_none=True)` |
| [BlackSheep](../../examples/with-blacksheep/) | ASGI | The shell is set as the router `fallback` |
| [Flask](../../examples/with-flask/) | WSGI | Needs two decorators for `/` and `/<path>` |
| [Robyn](../../examples/with-robyn/) | Rust-backed | Returns plain Python objects, which Robyn serializes |
| [Bottle](../../examples/with-bottle/) | WSGI | Set the JSON content type by hand |
| [Django](../../examples/with-django/) | WSGI | `JsonResponse(..., safe=False)`, because the payload is a list |
| [Emmett](../../examples/with-emmett/) | RSGI | Trailing slashes are stripped, so register `/api` |
| [Falcon](../../examples/with-falcon/) | WSGI | Use a *sink* for the catch-all |
| [Pyramid](../../examples/with-pyramid/) | WSGI | Needs an explicit response charset |
| [Quart](../../examples/with-quart/) | ASGI | Like Flask, but async |
| [Sanic](../../examples/with-sanic/) | ASGI | `strict_slashes=True` on the API route |
| [Tornado](../../examples/with-tornado/) | async | Handlers match in list order |

Each example has its own README and a small test.

Two frameworks are deliberately missing: [Hug](../../examples/with-hug/) does not import on Python 3.13+, and [Masonite](../../examples/with-masonite/) is a project framework that does not fit a single-file example. Their READMEs explain why.

## Using FastUI as a sub-application

You can also mount a whole FastUI app under a prefix of a bigger FastAPI app.
[`examples/sub_application`](../../examples/sub_application/) shows how, and answers [pydantic/FastUI#311](https://github.com/pydantic/FastUI/issues/311) and [#134](https://github.com/pydantic/FastUI/issues/134).

Next: [Where to go next](09-next-steps.md).
