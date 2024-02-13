from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.user_registration.as_view(), name="signup"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.UserProfileView.as_view(), name="profile"),
    path("edit/<int:pk>/", views.Editprofile.as_view(), name="edit"),
    path("passchange/", views.passchange.as_view(), name="passchange"),
    path("buy/<int:id>/", views.buy_car, name="buy"),
]
