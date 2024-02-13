from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from . import forms
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView
from user.models import Purchase, User
from cars.models import carModel


# Create your views here.
class user_registration(CreateView):
    form_class = forms.UserRegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Account created successfully")
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "login.html"

    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Logged in Successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Logged in information incorrect")
        return super().form_invalid(form)


def user_logout(request):

    logout(request)
    messages.success(request, "Log out successfully")
    return redirect("login")


class UserProfileView(CreateView):
    template_name = "profile.html"

    def get(self, request):
        context = Purchase.objects.filter(user=request.user)
        return render(request, "profile.html", {"context": context})


class Editprofile(UpdateView):
    model = User
    form_class = forms.UpdateForm
    template_name = "update.html"
    success_url = reverse_lazy("profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Update Profile"
        return context


class passchange(PasswordChangeView):
    template_name = "register.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        messages.success(self.request, "password changed !!")
        return super().form_valid(form)


def buy_car(request, id):
    data = carModel.objects.get(pk=id)
    qnt = data.quantity
    if qnt > 0:
        qnt -= 1
        data.quantity = qnt
        data.save()
        Purchase.objects.create(user=request.user, car=data)
        return redirect("profile")
    return render(request, "details.html", {"car": data})
