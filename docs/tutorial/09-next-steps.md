# 9. Where to go next

You now know the whole model: components as JSON, events for interaction, `ServerLoad` for partial updates, and `ModelForm` for input.
The rest is learning components and combining these ideas.

## Bigger examples in this repository

- [**Basic components gallery**](../../examples/basic_component_gallery/): one page showing many components, for browsing what exists.
- [**Personal portfolio**](../../examples/personal_portfolio/): a single-page profile built from `Heading`, `Image`, `Paragraph` and `LinkList`.
- [**ChatGPT-style chatbot**](../../examples/chatgpt/): streaming responses with server-sent events, a `ModelForm` input, and `pydantic-ai`. It is the most advanced example, and combines `ServerLoad`, `ModelForm` and `Table` from chapters 5 to 7.

## Ideas to try

- Build a to-do list: a `ModelForm` to add items, a `Table` to show them, and a `ServerLoad` to refresh the table after each add.
- Add authentication with a login form and a FastAPI dependency.
- Serve a FastUI app from a framework from [chapter 8](08-other-frameworks.md) that you already use.

## Official and community resources

- [FastUI repository](https://github.com/pydantic/FastUI), including its [demo app](https://github.com/pydantic/FastUI/tree/main/demo), the most complete reference there is
- [fastui-chat](https://github.com/shroominic/fastui-chat)
- [apscheduler-webui](https://github.com/Dragon-GCS/apscheduler-webui)
- [jrycw/edgedb-fastapi-mvp](https://github.com/jrycw/edgedb-fastapi-mvp)

Found something unclear or wrong? Please [open an issue](https://github.com/hasansezertasan/fastui-tutorials/issues).
