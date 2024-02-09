# FastUI Tutorials

I'm exploring FastUI features and capabilities, and in doing so, I'm developing entry-level examples.

FastUI doesn't have a documentation, so you need to figure out how to use it by looking at the source code (terrible idea if you don't know ReactJS) or by looking at the demo application (which is a bit complicated and hard to understand).

So this project (with simple examples) might be helpful for those who are new to FastUI.

## Examples

> Each example is a separate project and ordered by complexity.

- [Hello World](hello-world)
- [Random Number Generator](random-number-generator)
- [Admin Panel](admin-panel)

## Runing the examples

### Clone the repo

```shell
git clone https://github.com/hasansezertasan/fastui-tutorials.git
cd fastui-tutorials
```

### Install dependencies with poetry

```shell
poetry shell
poetry install
```

### Install dependencies with virtualenv

- Create and activate a virtual environment:

```shell
python3 -m venv venv
source venv/bin/activate
```

- Install requirements:

```shell
pip install -r '{{project-name}}/requirements.txt'
```

### Run the application

```shell
uvicorn {{project-name}}.main:app
```
