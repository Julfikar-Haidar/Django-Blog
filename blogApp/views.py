from django.shortcuts import render


# create my views

def index(request):
    return render(request, "index.html")


def getauthor(request,name):
    return render(request, "profile.html")


def getsingle(request, id):
    return render(request, "single.html")

# Create your views here.
