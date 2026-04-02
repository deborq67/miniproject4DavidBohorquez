from django.shortcuts import render
from .forms import SearchForm
from .organelle_ambiguity import initiate_search
from .models import SearchResult, SearchHistory
from django.utils import timezone
import csv
from django.http import HttpResponse

def search_view(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            df, total_records = initiate_search(form.cleaned_data["search_term"],request.user.email)
            # Save each row as a modal row in SearchResult.
            result_objects = []
            for _, row in df.iterrows():
                result = SearchResult.objects.create(
                    accession=row["Accession"],
                    title=row["Title"],
                    bp_length=row["BP Length"],
                    updated=row["Updated"],
                    ambiguity_percentage=row["Ambiguity Percentage"]
                )
                result_objects.append(result)

            # Save the search history as a modal row in SearchHistory.
            SearchHistory.objects.create(
                user=request.user,
                search_term=form.cleaned_data["search_term"],
                total_records=total_records,
                searched_at=timezone.now(),
            )

            return render(request, "search/results.html", {
                "results": result_objects,
                "organism": form.cleaned_data["search_term"],
                "total_records": total_records
            })
    else:
        form = SearchForm()
    return render(request, "index.html", {"form": form})

def history_view(request):
    history = SearchHistory.objects.filter(user=request.user).order_by("-searched_at")
    return render(request, "search/history.html", {"history": history})

def export_results_to_csv(request):
    model_class = SearchResult

    meta = model_class._meta
    field_names = ['accession','title','bp_length','updated','ambiguity_percentage']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="organellesearch_results.csv"'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in model_class.objects.all():
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response

def export_history_to_csv(request):
    model_class = SearchHistory
    meta = model_class._meta
    field_names = ['search_term','total_records','searched_at']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="organellesearch_history.csv"'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in model_class.objects.all():
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response

