"""Определяем схемы URLs для приложения usersapp"""

from django.urls import include, path

from . import views

app_name = "usersapp"
urlpatterns = [
    # Включить URL авторизации по умолчанию
    path("", include("django.contrib.auth.urls")),
    # Страница регистрации
    path("register/", views.register, name="register"),
]
