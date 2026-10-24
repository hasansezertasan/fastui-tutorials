# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""FastUI integration example for Django, as a single-file project."""

from __future__ import annotations

from typing import TYPE_CHECKING

from django.conf import settings
from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse, JsonResponse
from django.urls import path, re_path
from fastui import FastUI, prebuilt_html
from fastui import components as c

if TYPE_CHECKING:
    from django.http import HttpRequest

FastUI.model_rebuild()

if not settings.configured:
    settings.configure(
        DEBUG=True,
        ALLOWED_HOSTS=["*"],
        ROOT_URLCONF=__name__,
        SECRET_KEY="insecure-example-only",  # ruff: ignore[hardcoded-password-func-arg]
    )


def page(request: HttpRequest) -> JsonResponse:
    """Return the FastUI component tree.

    Returns:
        A JSON response containing the FastUI page components.
    """
    return JsonResponse(
        FastUI(root=[c.Heading(text="Hello World")]).model_dump(exclude_none=True),
        safe=False,
    )


def root(request: HttpRequest) -> HttpResponse:
    """Serve the FastUI React app shell, comes last as it matches all paths.

    Returns:
        An HTML page that loads the prebuilt FastUI app.
    """
    return HttpResponse(prebuilt_html(title="FastUI and Django Example"))


urlpatterns = [
    path("api/", page),
    re_path(r"^.*$", root),
]

app = get_wsgi_application()


def main() -> None:
    """Run the example with Django's development server."""
    execute_from_command_line(
        ["with-django", "runserver", "127.0.0.1:8000", "--noreload"],
    )


if __name__ == "__main__":
    main()
