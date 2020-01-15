from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

def home(request):
    if request.method == 'POST':
        entry = request.POST['form-entry']
        return redirect('app-home') #returns to the home page with the form
    else:
        return render(request,'pages/home.html')
        #render is for templates