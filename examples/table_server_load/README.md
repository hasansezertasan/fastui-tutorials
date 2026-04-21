# FastUI Table with ServerLoad Example

This example demonstrates how to pass an `id` from a table row to a `ServerLoad` component using `PageEvent` in FastUI.

This pattern is useful for loading additional details for a specific item when a user clicks on a row in a table.

## Key Concepts

1.  **`DisplayLookup` with `on_click`**: Each row in the table can have an `on_click` event.
2.  **`PageEvent` with `context`**: We use `PageEvent` to trigger an update to the page's state. The `context` dictionary allows us to pass variables from the row (using `{field_name}` syntax) into the page state.
3.  **`ServerLoad` with dynamic path**: The `ServerLoad` component listens for the `PageEvent` and uses the variable from the page state in its `path`.

## How to run

You can run this example using `uv`:

```bash
uv run main.py
```

Then open your browser at [http://localhost:8000/](http://localhost:8000/).
