# 3. Layout and page titles

Examples: [`simple_layout`](../../examples/simple_layout/) and [`dynamic_page_titles`](../../examples/dynamic_page_titles/)

## Containers

A bare list of components renders edge to edge.
`c.Page` is a container that adds standard page margins and holds other components:

```python
@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def page() -> list[AnyComponent]:
    return [
        c.Page(components=[c.Heading(text="I'm a heading in a page")]),
    ]
```

This is the pattern for the whole library: a component that can hold others takes a `components=[...]` list.
`c.Div`, which wraps its children in a plain `<div>` and takes a `class_name`, is the other container you will use all the time.

Run it with `uv run simple-layout` from `examples/simple_layout`.

## Page titles

The `title` you pass to `prebuilt_html` is only the *initial* title, shown until the API responds.
To change it from the API, return a `c.PageTitle`:

```python
@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def page() -> list[AnyComponent]:
    return [c.PageTitle(text="Updated | FastUI Dynamic Page Titles")]


@app.get("/{path:path}")
def root(path: str) -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title="Initial | FastUI Dynamic Page Titles"))
```

Watch the browser tab: it briefly shows "Initial", then switches.
`PageTitle` renders nothing visible. It exists only to set the title, so you can return it from any page.

Run it with `uv run dynamic-page-titles` from `examples/dynamic_page_titles`.

## Try it

- Put a `PageTitle` and a `Page` in the same list, as the [navigation example](04-navigation.md) does.
- Nest a `c.Div` inside a `c.Page`, and give it `class_name="border p-3"` (FastUI's prebuilt app ships with Bootstrap).

Next: [Navigation](04-navigation.md).
