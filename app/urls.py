from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("product/<int:product_id>", views.product_details, name="product_details"),
]