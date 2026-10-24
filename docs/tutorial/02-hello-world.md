# 2. Hello World

Example: [`examples/hello_world`](../../examples/hello_world/)

```shell
cd examples/hello_world
uv run hello-world
```

Open `http://127.0.0.1:8000` and you should see a heading.

## The code

```python
FastUI.model_rebuild()

app = FastAPI()


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def page() -> list[AnyComponent]:
    return [c.Heading(text="Hello World")]


@app.get("/{path:path}")
def root() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title="FastUI Hello World Example"))
```

Every FastUI app is these three pieces.

### 1. `FastUI.model_rebuild()`

The component models refer to each other by name (a `Page` contains other components, which can contain more).
Pydantic needs one call to resolve those references.
Put it near the top of your module and forget about it.

### 2. The API route returns components

`page()` returns a *list* of components.
`response_model=FastUI` tells FastAPI to validate and serialize the list as FastUI's schema.
`response_model_exclude_none=True` drops unset fields, so the JSON stays small and the React app applies its own defaults.

Without it, every unset optional field is sent as `null`. All the examples here set it.

### 3. The catch-all route returns the shell

`prebuilt_html(title=...)` returns the HTML page that loads the React app.
The route matches every path (`/{path:path}`), so `/`, `/about` and `/anything/else` all start the same app.
It comes last so it does not shadow `/api/`.

## Try it

- Change the heading `level` to 3, or add a second component to the list.
- Open `http://127.0.0.1:8000/api/` directly, and you will see the JSON the React app receives.

Next: [Layout and page titles](03-layout-and-titles.md).
