from django.urls import path
from .views import search_view, history_view

urlpatterns = [
    path("", search_view, name="search"),
    path("history/", history_view, name="history"),
]