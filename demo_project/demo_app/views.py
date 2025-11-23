from django.shortcuts import render


def demo_view(request):
    """
    Demo view showcasing all Basecoat components.
    """
    return render(request, "demo_app/demo.html")


def index_view(request):
    """
    Index view for the demo app.
    """
    return render(request, "demo_app/index.html")
