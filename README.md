# FastUI Tutorials

I'm exploring [FastUI][fastui] features and capabilities, and in doing so, I'm developing entry-level examples.

[FastUI][fastui] doesn't have a documentation, so you need to figure out how to use it by looking at the source code (terrible idea if you don't know ReactJS) or by looking at the demo application (which is a bit complicated and not very easy to understand).

So this project (with simple examples) might be helpful for those who are new to [FastUI][fastui].

## Examples

Each example is a separate project and ordered by complexity.

> You can find the instructions for running the examples in each project's README file.

- [Hello World](./examples/hello_world/)
- [Simple Layout](./examples/simple_layout/)
- [Dynamic Page Titles](./examples/dynamic_page_titles/)
- [Navbar Example](./examples/navigation/)
- [Random Number Generator](./examples/random_number_generator/)
- [Simple Form: BMI Calculator](./examples/simple_form/)
- [Basic Components Gallery](./examples/basic_component_gallery/)
- FastUI with other frameworks:
  - [Starlette Example](./examples/starlette_fastui/)
  - [Litestar Example](./examples/litestar_fastui/)
  - [Flask Example](./examples/flask_fastui/)
  - [Robyn Example](./examples/robyn_fastui/)
- FAQ:
  - [Sub Application](./examples/sub_application/)

### Other Examples

- [fastui-chat](https://github.com/shroominic/fastui-chat)
- [apscheduler-webui](https://github.com/Dragon-GCS/apscheduler-webui)
- [jrycw/edgedb-fastapi-mvp: MVP: EdgeDB and FastAPI Integration with svcs](https://github.com/jrycw/edgedb-fastapi-mvp)

<!-- Links -->
[fastui]: https://github.com/pydantic/FastUI

## Tasks

### `check`

```bash
mypy --strict .
```

### `lint`

```bash
codespell .
ruff check . --fix --unsafe-fixes
```

### `format`

```bash
ruff format .
```

### `run`

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### `test`

```bash
pytest -v -s
```
