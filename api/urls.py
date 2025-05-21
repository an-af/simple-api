from django.urls import path
from . import views

urlpatterns = [
    # testing 
    path("test", views.test, name="test"),
    # getAll Data 
    path("customer",views.getAllData, name="getAllData"),
    # get Data & delete by id
    path('customer/<int:customer_id>',views.operationDataByID, name="operationDataByID"),
    # update data
    path('customer/edit/<int:customer_id>', views.updateData, name="updateData")
]