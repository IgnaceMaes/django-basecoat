from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def demo_view(request: HttpRequest) -> HttpResponse:
    """
    Demo view showcasing all Basecoat components.
    """
    return render(request, "demo_app/demo.html")


def index_view(request: HttpRequest) -> HttpResponse:
    """
    Index view for the demo app.
    """
    return render(request, "demo_app/index.html")
