from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    # print('hello')
    return render(request, 'shorter_url_app/app_home.html')
    # return HttpResponse('hello')

