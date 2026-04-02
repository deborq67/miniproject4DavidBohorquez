from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from accounts.forms import EmailLoginForm
from results.views import history_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", LoginView.as_view(authentication_form=EmailLoginForm)),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("results.urls")),
    path("history/", history_view, name="history"),
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
]
