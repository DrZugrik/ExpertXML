# urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from bootstrap_test import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.home, name="home"),  # Путь для главной страницы
    path("admin/", admin.site.urls),
    path("about/", views.about, name="about"),
    path("gallery/", views.gallery, name="gallery"),
    path("pricing/", views.pricing, name="pricing"),
    path("contact/", views.contact, name="contact"),
#    path("upload/", views.upload, name="upload"),
    path("get_schemas/", views.get_schemas, name="get_schemas"),
    path("redact_form/", views.redact_form, name="redact_form"),
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("profile/", views.profile, name="profile"),
    path('upload/', views.upload_file, name='upload'),


]

# Добавляем обработчик для медиа-файлов только в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


