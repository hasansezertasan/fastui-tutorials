# FastUI Tutorials

I'm exploring [FastUI][fastui] features and capabilities, and in doing so, I'm developing entry-level examples.

[FastUI][fastui] doesn't have a documentation, so you need to figure out how to use it by looking at the source code (terrible idea if you don't know ReactJS) or by looking at the demo application (which is a bit complicated and not very easy to understand).

So this project (with simple examples) might be helpful for those who are new to [FastUI][fastui].

## Examples

Each example is a separate project and ordered by complexity.

> You can find the instructions for running the examples in each project's README file.

- [Hello World](./examples/hello-world/)
- [Simple Layout](./examples/simple-layout/)
- [Dynamic Page Titles](./examples/dynamic-page-titles/)
- [Navbar Example](./examples/navigation/)
- [Random Number Generator](./examples/random-number-generator/)
- [Simple Form: BMI Calculator](./examples/simple-form/)
- [Basic Components Gallery](./examples/basic-component-gallery/)
- FastUI with other frameworks:
  - [Starlette Example](./examples/starlette-fastui/)
  - [Litestar Example](./examples/litestar-fastui/)
  - [Flask Example](./examples/flask-fastui/)
  - [Robyn Example](./examples/robyn-fastui/)
- FAQ:
  - [Sub Application](./examples/sub-application/)
- FastUI with databases:
  - [SQLModel CRUD](./sqlalchemy-crud/): A simple CRUD application using [SQLModel][sqlmodel] and [FastUI][fastui].
  - [ODMantic CRUD](./sqlalchemy-crud/): A simple CRUD application using [ODMantic][odmantic] and [FastUI][fastui].
- FastUI Integrations and POCs:
  - [ChatGPT Example](./examples/chatgpt-example/)
  - [APScheduler UI](./apscheduler-ui/): A simple UI for [APScheduler][apscheduler] using [FastUI][fastui].
  - [OAuth2 UI](./oauth2-ui/): A simple UI for OAuth2 using [FastUI][fastui].
  - [Redis CLI](./redis-cli/): This example is inspired by [Flask Admin][flask-admin]'s Redis CLI implementation. It is a simple implementation of a Redis CLI using FastAPI and [FastUI][fastui].
  - [Libcloud UI](./libcloud-ui/): The original idea was to create something similar to [Flask Admin](flask-admin)'s File Admin but my mind changed and I decided to create a simple UI for managing multiple buckets in different cloud providers using [Apache Libcloud][libcloud] and [FastUI][fastui].

### Other Examples

- [fastui-chat](https://github.com/shroominic/fastui-chat)
- [apscheduler-webui](https://github.com/Dragon-GCS/apscheduler-webui)
- [jrycw/edgedb-fastapi-mvp: MVP: EdgeDB and FastAPI Integration with svcs](https://github.com/jrycw/edgedb-fastapi-mvp)

<!-- Links -->
[flask-admin]: https://github.com/flask-admin/flask-admin
[sqlmodel]: https://sqlmodel.tiangolo.com/
[odmantic]: https://github.com/art049/odmantic/
[fastui]: https://github.com/pydantic/FastUI
[apscheduler]: https://github.com/agronholm/apscheduler
[libcloud]: https://github.com/apache/libcloud

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
shfmt -l -w scripts/*.sh
```

### `run`

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### `test`

```bash
pytest -v -s
```
