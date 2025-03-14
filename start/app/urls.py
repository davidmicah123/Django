from django.urls import path
from . import views

urlpatterns = [
    path("one", views.func_one, name="func_one"),
    path("two", views.func_two, name="func_two"),
]