from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    # print('hello')
    return render(request, 'app_home.html')
    # return HttpResponse('hello')