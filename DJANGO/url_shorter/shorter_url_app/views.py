from django.shortcuts import render
from .models import Shorter_url
from django.http import HttpResponse
from django.utils.crypto import get_random_string


import random

# Create your views here.


def home(request):
    if request.method == 'POST':
        url = request.POST['url']
        Shorter_url.objects.create(url = url)
        return render(request, 'shorter_url_app/my_urls.html', )
    else:
        # return HttpResponse('shorter_url_app/app_home.html')
        return render(request, 'shorter_url_app/app_home.html', )


def url_strgen(url):
    short_url_id = get_random_string(legnth=20) #renames url, and resizing 
    resized_url = Shorter_url.objects.create(shorty = short_url_id) #saves to the database ??
    resized_url.save() #calls the variable assigned to the DB
    # print(short_url_id) 
    print(resized_url)


    
# TODO: supply both shorty and url from the Model in the create
#Pass both the short code and the long url in the create()

# def url_redirect():