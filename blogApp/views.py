from django.shortcuts import render,HttpResponse

# create my views

def index(request):
    return HttpResponse("<h1>This is my template</h1>")


# Create your views here.
