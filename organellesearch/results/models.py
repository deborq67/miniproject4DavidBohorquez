from django.db import models
from django.conf import settings

class SearchResult(models.Model):
    accession = models.CharField(max_length=50)
    title = models.TextField()
    bp_length = models.IntegerField()
    updated = models.CharField(max_length=50)
    ambiguity_percentage = models.FloatField(null=True)

class SearchHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    search_term = models.CharField(max_length=255)
    total_records = models.IntegerField()
    searched_at = models.DateTimeField(auto_now_add=True)
    results = models.ManyToManyField(SearchResult)
