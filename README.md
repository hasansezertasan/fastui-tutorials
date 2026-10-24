# FastUI Tutorials

Learn [FastUI][fastui], the library for building web UIs in pure Python, with no JavaScript.

[FastUI][fastui] has no official documentation, so you would otherwise have to read its source (a bad idea if you do not know ReactJS) or its demo application (which is fairly complicated).
This repository is a step-by-step tutorial backed by small, runnable examples.

## Start here

Read the **[tutorial](./docs/tutorial/README.md)**. It takes you from "what is FastUI" to forms, tables and partial updates in nine short chapters, each linked to a runnable example:

1. [How FastUI works](./docs/tutorial/01-how-fastui-works.md)
2. [Hello World](./docs/tutorial/02-hello-world.md)
3. [Layout and page titles](./docs/tutorial/03-layout-and-titles.md)
4. [Navigation](./docs/tutorial/04-navigation.md)
5. [Loading content on demand](./docs/tutorial/05-server-load.md)
6. [Forms](./docs/tutorial/06-forms.md)
7. [Tables](./docs/tutorial/07-tables.md)
8. [Other web frameworks](./docs/tutorial/08-other-frameworks.md)
9. [Where to go next](./docs/tutorial/09-next-steps.md)

You need Python 3.11+ and [uv](https://docs.astral.sh/uv/). Each example is its own project, and its README says how to run it.

## All examples

Each example is a separate project and ordered by complexity.

> You can find the instructions for running the examples in each project's README file.

- [Hello World](./examples/hello_world/)
- [Simple Layout](./examples/simple_layout/)
- [Dynamic Page Titles](./examples/dynamic_page_titles/)
- [Navbar Example](./examples/navigation/)
- [Random Number Generator](./examples/random_number_generator/)
- [Simple Form: BMI Calculator](./examples/simple_form/)
- [Basic Components Gallery](./examples/basic_component_gallery/)
- [Table with Detail Pages](./examples/table_server_load/)
- [ChatGPT-style Chatbot (pydantic-ai)](./examples/chatgpt/)
- [Personal Portfolio](./examples/personal_portfolio/)
- FastUI with other frameworks:
  - [Starlette Example](./examples/with-starlette/)
  - [Litestar Example](./examples/with-litestar/)
  - [BlackSheep Example](./examples/with-blacksheep/)
  - [Flask Example](./examples/with-flask/)
  - [Robyn Example](./examples/with-robyn/)
  - [Bottle Example](./examples/with-bottle/)
  - [Django Example](./examples/with-django/)
  - [Emmett Example](./examples/with-emmett/)
  - [Falcon Example](./examples/with-falcon/)
  - [Pyramid Example](./examples/with-pyramid/)
  - [Quart Example](./examples/with-quart/)
  - [Sanic Example](./examples/with-sanic/)
  - [Tornado Example](./examples/with-tornado/)
  - Not implemented, with the reasons why: [Hug](./examples/with-hug/) and [Masonite](./examples/with-masonite/)
- FAQ:
  - [Sub Application](./examples/sub_application/)

### Other Examples

- [fastui-chat](https://github.com/shroominic/fastui-chat)
- [apscheduler-webui](https://github.com/Dragon-GCS/apscheduler-webui)
- [jrycw/edgedb-fastapi-mvp: MVP: EdgeDB and FastAPI Integration with svcs](https://github.com/jrycw/edgedb-fastapi-mvp)

<!-- Links -->
[fastui]: https://github.com/pydantic/FastUI

## Tasks

### `check`, `lint` and `format`

```bash
uvx prek run --all-files --show-diff-on-failure
```

### `test`

```bash
uv run --locked pytest -q
```
