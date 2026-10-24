# FastUI Table with Detail Pages

> This example is explained step by step in the [tutorial](../../docs/tutorial/07-tables.md).

A table of users where clicking an ID opens a detail page for that user.

> The directory is still called `table_server_load` because it started as a `ServerLoad` demo.
> It now uses `GoToEvent`, because passing a row value through `PageEvent` context does not work.
> See [chapter 7](../../docs/tutorial/07-tables.md#why-not-pageevent-context) for the details.

## Key Concepts

1.  **`Table` with `DisplayLookup`**: `data` and `data_model` supply the rows and the headers, and `columns` picks and orders the fields.
2.  **`on_click` with `GoToEvent`**: `GoToEvent(url="/user/{id}")` navigates when the cell is clicked. `{id}` is replaced with the clicked row's `id`.
3.  **A route per detail page**: `/user/2` in the browser is served by `/api/user/2`, as in every FastUI app.

## How to run

### Change directory to the example

```shell
cd examples/table_server_load
```

### Run the application

```shell
uv run table-server-load
```

Then open your browser at [http://localhost:8000/](http://localhost:8000/).
