from django.shortcuts import render
from django.http import HttpResponse
from street_biter_app.models import Street_biter


def home(request):
    return render(request, 'street_biter_app/home.html')


def about(request):
    return render(request, 'street_biter_app/about.html')
    

    #marker information from user coordinates 
def details(request):
    # sweetspot = Street_biter.objects.filter(user = request.user, latitude=request.latitude, longitude=request.longitude).first()
    sweetspot = Street_biter.objects.all()
    return render(request, 'street_biter_app/details.html', {'sweetspot': sweetspot})