from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'recipes/page/home.html')


def recipe(request, id):
    return render(request,'recipes/page/recipe-views.html')
