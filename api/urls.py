from django.urls import path
from . import views

urlpatterns = [
    path("hai", views.hello_world, name="hello_world")
]