# FastUI Tutorial

A hands-on introduction to [FastUI][fastui]: build user interfaces in pure Python, with no JavaScript to write.

FastUI has no official tutorial, so this one walks through the runnable projects in [`examples/`](../../examples/).
Each chapter introduces one idea, explains the code, and links to the example you can run.

## Before you start

You need Python 3.11+ and [uv](https://docs.astral.sh/uv/).
Clone the repository once and run every example from it:

```shell
git clone https://github.com/hasansezertasan/fastui-tutorials.git
cd fastui-tutorials
```

You do not need to know React.
Basic familiarity with [FastAPI](https://fastapi.tiangolo.com/) and [Pydantic](https://docs.pydantic.dev/) helps for the middle chapters.

## Chapters

| # | Chapter | You will learn | Example |
| --- | --- | --- | --- |
| 1 | [How FastUI works](01-how-fastui-works.md) | The model: the server returns JSON, a React app renders it | none |
| 2 | [Hello World](02-hello-world.md) | The three pieces every FastUI app has | [hello_world](../../examples/hello_world/) |
| 3 | [Layout and page titles](03-layout-and-titles.md) | Containers, and changing the browser title | [simple_layout](../../examples/simple_layout/), [dynamic_page_titles](../../examples/dynamic_page_titles/) |
| 4 | [Navigation](04-navigation.md) | Several pages, a navbar and links, and a shared layout function | [navigation](../../examples/navigation/) |
| 5 | [Loading content on demand](05-server-load.md) | Events and `ServerLoad` for partial updates | [random_number_generator](../../examples/random_number_generator/) |
| 6 | [Forms](06-forms.md) | Turning a Pydantic model into a validated form | [simple_form](../../examples/simple_form/) |
| 7 | [Tables](07-tables.md) | Rendering data, and linking each row to a detail page | [table_server_load](../../examples/table_server_load/) |
| 8 | [Other web frameworks](08-other-frameworks.md) | FastUI is not tied to FastAPI | [with-flask](../../examples/with-flask/) and 12 more |
| 9 | [Where to go next](09-next-steps.md) | Bigger examples, and ideas to try | [chatgpt](../../examples/chatgpt/), [personal_portfolio](../../examples/personal_portfolio/) |

[fastui]: https://github.com/pydantic/FastUI
