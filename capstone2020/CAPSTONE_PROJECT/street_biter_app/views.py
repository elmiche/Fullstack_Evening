from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'street_biter_app/home.html')


def about(request):
    return render(request, 'street_biter_app/about.html')
    

    
#TODO add view that saves lat and longs to street_biter model.