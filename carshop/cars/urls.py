from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("addcar/", views.carview.as_view(), name="addcar"),
]
