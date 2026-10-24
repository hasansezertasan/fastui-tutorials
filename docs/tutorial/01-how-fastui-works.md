# 1. How FastUI works

Before any code, it helps to know what FastUI actually is, because it works differently from most Python web tools.

## The model

A normal server-rendered app returns HTML.
A FastUI app returns **JSON that describes a user interface**:

```json
[{"type": "Heading", "text": "Hello World", "level": 1}]
```

That JSON is a tree of *components*, such as headings, tables, forms and buttons.
Your Python code builds it with Pydantic models: `c.Heading(text="Hello World")` is a model that serializes to the object above.

Something has to turn the JSON into pixels.
That is a prebuilt React application, published as the `@pydantic/fastui-prebuilt` npm package.
Your server hands the browser a tiny HTML page that loads it, and from then on the React app does the rendering.

## What happens on each page load

```text
Browser                         Your server
   |  GET /about                    |
   |------------------------------->|  catch-all route returns the HTML shell
   |<-------------------------------|  (loads the React app)
   |                                |
   |  GET /api/about                |
   |------------------------------->|  your function returns component JSON
   |<-------------------------------|
   |                                |
   | React renders the components   |
```

Two rules fall out of this, and every example in this repository follows them:

1. **The URL the browser shows is `/x`; the data comes from `/api/x`.**
   The React app asks for the same path with `/api` in front.
2. **One catch-all route returns the HTML shell for any path.**
   It must be registered *last*, or it would swallow the `/api/...` routes.

## Why this design is useful

- You write the UI in the same language, and the same type system, as your backend.
- The frontend and backend agree on a contract, the component schema, so there is nothing to keep in sync by hand.
- Navigation, partial updates and form submission are all expressed as *events* that you attach to components, still in Python.

## The trade-offs

- You pick from FastUI's components. Anything custom means writing React.
- The prebuilt app is loaded from a CDN, so pages need network access.
- FastUI is young and its documentation is thin, which is why this tutorial exists.

Next: [Hello World](02-hello-world.md).
