# django_project/urls.py
from django.contrib import admin
from django.urls import path, include # new
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")), 
    path("rating/", include("rating.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
]
