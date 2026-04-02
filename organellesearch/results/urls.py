from django.urls import path
from .views import search_view, export_history_to_csv, export_results_to_csv, download_results_page, download_history_page

urlpatterns = [
    path("", search_view, name="search"),
    path("results/download/", export_results_to_csv, name="results_downloads"),
    path("history/download/", export_history_to_csv, name="history_download"),
    path("results/download/page/", download_results_page, name="results_download_page"),
    path("history/download/page/", download_history_page, name="history_download_page"),
]