# 7. Tables

Example: [`examples/table_server_load`](../../examples/table_server_load/)

```shell
cd examples/table_server_load
uv run table-server-load
```

This chapter combines models, events and `ServerLoad` into a master/detail view: click a row's ID to load its details underneath.

## Data and columns

```python
class User(BaseModel):
    id: int = Field(title="ID")
    name: str = Field(title="Name")
    role: str = Field(title="Role")


c.Table(
    data=users,
    data_model=User,
    columns=[
        DisplayLookup(field="id", on_click=PageEvent(name="user-details", context={"user_id": "{id}"})),
        DisplayLookup(field="name"),
        DisplayLookup(field="role"),
    ],
)
```

- `data` is a list of model instances and `data_model` is their type, which supplies the column headers (the field `title`s).
- `columns` is a list of `DisplayLookup`, one per column, in display order. Each says which field to show, and can carry its own event.
- `"{id}"` is a placeholder filled in from the clicked row. Here, `context={"user_id": "{id}"}` attaches the row's ID to the event.

## Connecting to `ServerLoad`

```python
c.ServerLoad(
    path="/api/user-details/{user_id}",
    load_trigger=PageEvent(name="user-details"),
    components=[c.Text(text="Select a user to see details...")],
)
```

When the `user-details` event fires, the `ServerLoad` fills `{user_id}` in its path from the event's context and fetches it:

```python
@app.get("/api/user-details/{user_id}", response_model=FastUI, response_model_exclude_none=True)
def user_details(user_id: int) -> list[AnyComponent]:
    ...
```

This is an ordinary FastAPI path parameter, with all of FastAPI's validation.
The route returns a fragment, as in [chapter 5](05-server-load.md), and the React app places it where the `ServerLoad` is.

This is the central FastUI pattern for interactive pages: *named events carry context to server-loaded fragments*.

## Try it

- Add a `DisplayLookup` with `field="role"` and an `on_click` that loads a role description.
- Return `c.Heading` and `c.Paragraph` for an unknown user instead of a bare `Text`.

Next: [Other web frameworks](08-other-frameworks.md).
