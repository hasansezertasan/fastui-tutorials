# 4. Navigation

Example: [`examples/navigation`](../../examples/navigation/)

```shell
cd examples/navigation
uv run navigation
```

## One route per page

Remember the rule from [chapter 1](01-how-fastui-works.md): the page at `/about` is served by the route at `/api/about`.
So adding a page means adding an API route:

```python
@app.get("/api/about", response_model=FastUI, response_model_exclude_none=True)
def page_about() -> list[AnyComponent]:
    return layout(c.Text(text="About Page!"), title="About Page!")
```

The catch-all HTML route needs no change, because it already serves every path.

## Events

Links in FastUI do not use `href`.
Instead you attach an **event** to a component, and the React app reacts to it.
`GoToEvent` navigates:

```python
c.Link(
    components=[c.Text(text="About")],
    on_click=GoToEvent(url="/about"),
    active="startswith:/about",
)
```

- `on_click` is the event to fire.
- `active="startswith:/about"` highlights the link while the current URL starts with `/about`.
- `GoToEvent(url="https://...", target="_blank")` opens an external URL in a new tab.

Navigation happens in the browser without a full page reload: the React app updates the URL and fetches `/api/about`.

## A shared layout

Every page needs the same navbar, so the example wraps it in a plain Python function:

```python
def layout(*components: AnyComponent, title: str) -> list[AnyComponent]:
    return [
        c.PageTitle(text=title),
        c.Navbar(title="Site Title", title_event=GoToEvent(url="/"), start_links=[...]),
        c.Page(components=components),
    ]
```

There is no template inheritance to learn: a layout is just a function that returns components.
This is the main way FastUI apps share structure.

## Try it

- Add a fourth page, and a link to it in the navbar.
- Use `end_links=[...]` on the `Navbar` to put links on the right.

Next: [Loading content on demand](05-server-load.md).
