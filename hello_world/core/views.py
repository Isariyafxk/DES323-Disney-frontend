from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def home(request):
    context = {}
    return render(request, "webpages/home.html", context=context)

def register(request):
    context = {}
    return render(request, "webpages/register.html", context=context)

def login(request):
    context = {}
    return render(request, "webpages/login.html", context=context)

def places(request):
    context = {}
    return render(request, "webpages/places.html", context=context)