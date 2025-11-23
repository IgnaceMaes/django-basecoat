from django.urls import path

from . import views

app_name = "demo_app"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("demo/", views.demo_view, name="demo"),
]
