from django.shortcuts import render
from django.http import JsonResponse
from django.template import loader
from django.http import HttpResponse
import pandas as pd
from .models import *
from models.models import DisneylandReview

def import_data_csv(request):
    csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS4EPpyFHzOACG9rfzqk3bJ0PbCawzX24IgYrYptGgi0cvDo4IH7frGmYuNBdLBzYuW0MHxv8EYoBDA/pub?output=csv'
    df = pd.read_csv(csv_url)
    data_sets = df[["Review_ID","Rating","Year_Month","Review_Text","Branch"]]
    sucesss = []
    errors = []
    for index, row in data_sets.iterrows():
        instance = DisneylandReview(
            Review_ID = int(row['Review_ID']),
            Rating = int(row['Rating']),
            Year = row['Year_Month'],
            Text = row['Review_Text'],
            Branch = row['Branch'],
        )
        try:
            instance.save()
            sucesss.append(index)
        except:
            errors.append(index)
    return JsonResponse({"success_indexes":sucesss,"error_index":errors})

def get_data_disney(request):
    review_texts = DisneylandReview.objects.all().values('Review_ID', 'Text')[:10]
    print(review_texts)
    context_data = {
        "comment":  review_texts


    }
    
    return render(request, '../../hello_world/templates/webpages/places.html', context=context_data)






# def get_data(request):
#      # Assuming that your model has 'Review' and 'Text' fields
#     review_texts = DisneylandReview.objects.all().values('Review_ID', 'Text')
#     context_data = {
#         "filter_type": "All",
#         "reviews": review_texts  # Change "review" to "reviews" for consistency
#     }

#     return render(request, 'places.html', context=context_data)
