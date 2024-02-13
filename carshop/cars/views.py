from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from . import models
from . import forms
from django.urls import reverse_lazy
from cars.forms import CommentForm


# Create your views here.
class carview(CreateView):
    model = models.carModel
    form_class = forms.carForm
    template_name = "add_car.html"
    success_url = reverse_lazy("addcar")
