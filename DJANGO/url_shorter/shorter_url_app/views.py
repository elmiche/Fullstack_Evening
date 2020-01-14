from django.shortcuts import render, redirect
from .models import Shorter_url
from django.http import HttpResponse
from django.utils.crypto import get_random_string


import random

# Create your views here.


def home(request):
    if request.method == 'POST':
        url = request.POST['url']
        short_url_id = get_random_string(length=5) #renames url, and resizing 
        Shorter_url.objects.create(url = url, shorty = short_url_id) #saves to the database
        # print(short_url_id) 
        return redirect('my-urls/')
    else:
        # return HttpResponse('shorter_url_app/app_home.html')
        return render(request, 'shorter_url_app/app_home.html', )



def url_list(request):
    urlshorties = Shorter_url.objects.all()
    context ={
        'shorties' : urlshorties
    }
    return render(request,'shorter_url_app/my_urls.html', context)


def url_redirect(request, shorty): #this shorty comes from my_urls (2nd shorty)
    clicky = Shorter_url.objects.get(shorty = shorty) #first shorty is from model, 2nd is from paremeter
    return redirect(clicky.url)