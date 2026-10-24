# 5. Loading content on demand

Example: [`examples/random_number_generator`](../../examples/random_number_generator/)

```shell
cd examples/random_number_generator
uv run random-number-generator
```

So far every page was loaded whole.
Often you want to refresh *part* of a page, such as a button, a panel or a list, without reloading anything else.
That takes two components working together: an event and a `ServerLoad`.

## `ServerLoad`

`c.ServerLoad` is a placeholder that fetches its contents from another API route:

```python
c.ServerLoad(
    path="/replace",
    load_trigger=PageEvent(name="replace"),
    components=[c.Button(text="Random: 42", on_click=PageEvent(name="replace"))],
)
```

- `path` is the API route to call (here `/api/replace`; FastUI adds the `/api` prefix).
- `components` is what to show *before* the first load.
- `load_trigger` names an event that makes it fetch again.

## `PageEvent`

`PageEvent(name="replace")` is a named signal that stays inside the current page.
Anything on the page can fire it, and anything can listen.
Here the button fires it with `on_click`, and the `ServerLoad` listens with `load_trigger`.

## The loop

1. You click the button, which fires the `replace` event.
2. The `ServerLoad` hears it and calls `GET /api/replace`.
3. That route returns a fresh `ServerLoad` containing a new button, and the React app swaps it in.

```python
@app.get("/api/replace", response_model=FastUI, response_model_exclude_none=True)
async def modal_view() -> list[AnyComponent]:
    await asyncio.sleep(0.5)
    return [c.ServerLoad(...)]
```

The route returns the same `ServerLoad` so the button keeps working.
The `sleep` only makes the loading state visible. Remove it and the update is instant.

Notice that the response is a fragment, not a page: no navbar, no `Page`.
Any API route can return a fragment, and `ServerLoad` is how you place it.

## Try it

- Change the button text, or return a `c.Text` instead of a button from `/api/replace` and watch the button disappear.
- Add a second button that fires the same event.

Next: [Forms](06-forms.md).
