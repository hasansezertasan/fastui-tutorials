# FastUI Tutorials

I'm exploring the capabilities of FastUI.

## Examples

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
