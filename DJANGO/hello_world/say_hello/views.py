from django.shortcuts import render

# Create your views here.
#views = functions 

def index(request):
    return render(request, 'index.html')
