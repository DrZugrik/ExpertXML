from django.contrib import admin
from django.urls import path
from bootstrap_test import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login  # Изменено на login


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  # добавлен корневой путь для вашей домашней страницы
    path("about/", views.about, name="about"),  # добавлен путь для страницы "About"
    path("gallery/", views.gallery, name="gallery"),  # добавлен путь для страницы "Gallery"
    path("pricing/", views.pricing, name="pricing"),  # добавлен путь для страницы "Pricing"
    path("contact/", views.contact, name="contact"),  # добавлен путь для страницы "Contact"

    path("upload/", views.upload, name="upload"),  # добавлен путь для страницы "Загрузка"

    path('get_schemas/', views.get_schemas, name='get_schemas'),

    path("redact_form/", views.redact_form, name="redact_form"),  # добавлен путь для страницы "redact_form"

    path("login/", views.login_view, name="login"),  # Изменено имя представления на login_view

    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    path('profile/', views.profile, name='profile'),
]
