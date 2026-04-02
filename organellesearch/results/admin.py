from django.contrib import admin

from .models import SearchHistory




class HistoryAdmin(admin.ModelAdmin):
    date_hierarchy = "searched_at"
    fieldsets = [
        (None, {"fields": ["search_term", "total_records"]}),
    ]
    list_display = ["user","search_term", "total_records", "searched_at"]
    list_filter = ["searched_at"]
    search_fields = ["search_term"]
admin.site.register(SearchHistory, HistoryAdmin)
