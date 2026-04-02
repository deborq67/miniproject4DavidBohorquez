from django.urls import path
from .views import search_view, export_history_to_csv, export_results_to_csv

urlpatterns = [
    path("", search_view, name="search"),
    path("download_results/", export_results_to_csv, name="download"),
    path("download_history/", export_history_to_csv, name="download"),
]