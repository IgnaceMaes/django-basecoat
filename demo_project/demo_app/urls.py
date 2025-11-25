from django_distill import distill_path

from . import views

app_name = "demo_app"

urlpatterns = [
    distill_path(
        "",
        views.index_view,
        name="index",
        distill_file="index.html",
    ),
    distill_path(
        "demo/",
        views.demo_view,
        name="demo",
    ),
]
