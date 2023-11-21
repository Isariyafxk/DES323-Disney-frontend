from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import *

def import_data_csv(request):
    csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR2ZacBZdkvDSD-JXC4Cj4ExDPmwx7BuYk8lo3W8aFNfWLfa2W1k2EvdJhf6a3LJpTMcyophf9Y4KUi/pub?output=csv'
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