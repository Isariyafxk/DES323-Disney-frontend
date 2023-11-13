from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def home(request):
    context = {}
    return render(request, "webpages/home.html", context=context)

def places(request):
    context = {}
    return render(request, "webpages/places.html", context=context)

def helpcenter(request):
    context = {}
    return render(request, "webpages/helpcenter.html", context=context)

def aboutus(request):
    context = {}
    return render(request, "webpages/aboutus.html", context=context)
