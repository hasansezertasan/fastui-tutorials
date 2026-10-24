# 7. Tables

Example: [`examples/table_server_load`](../../examples/table_server_load/)

```shell
cd examples/table_server_load
uv run table-server-load
```

This chapter builds a list of users where clicking an ID opens that user's detail page.

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
        DisplayLookup(field="id", on_click=GoToEvent(url="/user/{id}")),
        DisplayLookup(field="name"),
        DisplayLookup(field="role"),
    ],
)
```

- `data` is a list of model instances and `data_model` is their type, which supplies the column headers (the field `title`s).
- `columns` is a list of `DisplayLookup`, one per column, in display order. Each says which field to show, and can carry its own event.
- `"{id}"` in the event URL is replaced with the `id` of the row that was clicked.

## The detail page

Clicking the ID fires a `GoToEvent`, so the browser moves to `/user/2`.
As always, that page is served by the matching API route:

```python
@app.get("/api/user/{user_id}", response_model=FastUI, response_model_exclude_none=True)
def user_details(user_id: int) -> list[AnyComponent]:
    ...
    return [
        c.PageTitle(text=f"Details for {user.name}"),
        c.Page(components=[c.Heading(...), c.Paragraph(...), back_link()]),
    ]
```

`user_id` is an ordinary FastAPI path parameter, with all of FastAPI's validation.
`back_link()` is a plain Python helper that returns a `Link` with `GoToEvent(url="/")`, in the same spirit as the `layout()` function from [chapter 4](04-navigation.md).

## Why not `PageEvent` context?

The obvious design, given [chapter 5](05-server-load.md), is to keep the table and the details on one page:
fire a `PageEvent` carrying the row's ID and let a `ServerLoad` fetch the details.

```python
# Does NOT work as you would hope
DisplayLookup(field="id", on_click=PageEvent(name="user-details", context={"user_id": "{id}"}))
```

This is a trap, and the repository's example used to fall into it.
With the prebuilt app that FastUI loads at the time of writing (`@pydantic/fastui-prebuilt` 0.0.26), the `{id}` row placeholder is substituted in a `GoToEvent` URL, but not inside a `PageEvent`'s `context`.
The `ServerLoad` therefore requests `/api/user-details/%7Bid%7D`, the literal text `{id}`, and the server answers `422`.

A second trap hides nearby: a `ServerLoad` `path` must *not* start with `/api`, because the frontend adds that prefix itself.
`path="/api/user-details/{user_id}"` becomes `/api/api/user-details/...`.

If you find a version of the prebuilt app where row values reach `PageEvent` context, the two-component design becomes possible again.
Until then, a detail page per row is the reliable pattern, and it is the one FastUI's own demo uses.

## Try it

- Add a `DisplayLookup(field="name", on_click=GoToEvent(url="/user/{id}"))` so the name links too.
- Return a proper 404 for an unknown user by raising `fastapi.HTTPException(status_code=404)`.

Next: [Other web frameworks](08-other-frameworks.md).
