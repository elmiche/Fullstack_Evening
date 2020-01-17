from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Basic_crud_app


# Create your views here.

def create(request):
    if request.method == 'POST':
        entry = request.POST['form-entry']
        Basic_crud_app.objects.create(message = entry) #connect view to Model
        return redirect('app-home') #returns to the home page with the form
    else:
        return render(request,'pages/home.html')
        #render is for templates

def read(request):
    items = Basic_crud_app.objects.all()
    context ={
        'blurbs' : items
    }
    return render(request, 'pages/index.html', context)
                    #from inside the crud_app dir

    # this need a render because it needs context and a template
    #does this need a context dictionary? YES
    #ALSO should I reference a url or should I make a template and refence it with render... MAKE TEMPLATE and RENDER

    # TODO - add redirect to index read view





