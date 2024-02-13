from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("addbrand/", views.add_brand.as_view(), name="addbrand"),
]
