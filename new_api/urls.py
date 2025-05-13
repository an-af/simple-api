from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.new_hello_worlds,name="hello"),
    path("waktu", views.waktu_sekarang, name="waktu")
]