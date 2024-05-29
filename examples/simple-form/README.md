# Simple Form: BMI Calculator

This example is inspired by [PyWebIO][pywebio] [documentation][pywebio-hello-world]. It is the first example in the documentation so I thought it would be a good idea to use it as a starting point for forms in FastUI.

Used Components:

- `PageTitle`
- `Page`
- `Heading`
- `Paragraph`
- `ModelForm`

<!-- Links -->
[pywebio]: https://github.com/pywebio/PyWebIO
[pywebio-hello-world]: https://pywebio.readthedocs.io/en/latest/#hello-world

## Running the examples

### Clone the repo

```shell
git clone https://github.com/hasansezertasan/fastui-tutorials.git
cd fastui-tutorials
```

### Change directory to the example

```shell
cd examples/simple-form
```

### Create a virtual environment

- Create and activate a virtual environment:

```shell
python3 -m venv venv
source venv/bin/activate
```

### Install the requirements

```shell
pip install -r 'requirements.txt'
```

### Run the application

```shell
uvicorn main:app
```
