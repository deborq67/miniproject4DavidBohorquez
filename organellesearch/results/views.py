from django.shortcuts import render
from .forms import SearchForm
from .organelle_ambiguity import initiate_search
from .models import SearchResult, SearchHistory

def search_view(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        print(form.errors)
        if form.is_valid():
            df, total_records = initiate_search(
                form.cleaned_data["search_term"],
                request.user.email
            )

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
            history = SearchHistory.objects.create(
                user=request.user,
                search_term=form.cleaned_data["search_term"],
                total_records=total_records
            )
            history.results.set(result_objects)

            return render(request, "search/results.html", {
                "results": result_objects,
                "organism": form.cleaned_data["search_term"],
                "total_records": total_records
            })
    else:
        form = SearchForm()
    return render(request, "index.html", {"form": form})