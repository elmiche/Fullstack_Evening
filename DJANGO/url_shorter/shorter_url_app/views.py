from django.shortcuts import render
from .models import Shorter_url
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method == 'POST':
        url = request.POST['url']
        Shorter_url.objects.create(url = url)
    else:
        return HttpResponse('shorter_url_app/app_home.html')
        # return render(request, 'shorter_url_app/app_home.html')
    # return HttpResponse('hello')

