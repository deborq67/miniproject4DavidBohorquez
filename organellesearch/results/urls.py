from django.urls import path
from .views import search_view, export_to_csv

urlpatterns = [
    path("", search_view, name="search"),
    path("download/", export_to_csv, name="download"),
]