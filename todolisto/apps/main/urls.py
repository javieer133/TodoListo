from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views


# noinspection PyInterpreter
urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('home', views.index, name="home"),
]
