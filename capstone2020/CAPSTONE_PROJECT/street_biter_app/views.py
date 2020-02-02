from django.shortcuts import render, redirect
from django.http import HttpResponse
from street_biter_app.models import Street_biter
# from street_biter_app.forms import Street_biter_form


def home(request):
    if request.method == 'POST':
        form = Street_biter(request.POST)
    else:
        return render(request, 'street_biter_app/home.html')


def about(request):
    return render(request, 'street_biter_app/about.html')
    

    #marker information from user coordinates 
def details(request):
    # sweetspot = Street_biter.objects.filter(user = request.user, latitude=request.latitude, longitude=request.longitude).first()
    sweetspot = Street_biter.objects.first()
    return render(request, 'street_biter_app/details.html', {
            'sweetspot': sweetspot, 
            })

def save_details():
    form = Street_biter_form(request.POST)
    form.save()
    return redirect('details-view')