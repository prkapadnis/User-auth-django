import imp
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_user, name="login_user"),
    path("register_user/", views.register_user, name="register_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("dashboard/", views.dashboard, name="dashboard"),
]