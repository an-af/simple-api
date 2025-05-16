from django.urls import path
from . import views

urlpatterns = [
    path("test", views.test, name="test"),
    path("customer",views.getAllData, name="getAllData"),
    path("customer/create",views.addData, name="addData"),
    path('customer/<int:customer_id>',views.getDataByID, name="getDataByID")
]