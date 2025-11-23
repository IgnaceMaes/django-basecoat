from django.urls import path
from .views import demo_view, DemoView

app_name = "basecoat_cotton"

urlpatterns = [
    path("demo/", demo_view, name="demo"),
    # Alternative: path("demo/", DemoView.as_view(), name="demo"),
]
