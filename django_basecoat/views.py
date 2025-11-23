from django.shortcuts import render
from django.views.generic import TemplateView


class DemoView(TemplateView):
    """
    Demo view showcasing all Basecoat components.
    """
    template_name = "basecoat_cotton/demo.html"


def demo_view(request):
    """
    Function-based view for the component demo.
    """
    return render(request, "basecoat_cotton/demo.html")
