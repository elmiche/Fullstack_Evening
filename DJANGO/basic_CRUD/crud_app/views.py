from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Basic_crud_app


# Create your views here.

def create(request):
    if request.method == 'POST':
        entry = request.POST['form-entry']
        Basic_crud_app.objects.create(message = entry) #connect view to Model
        return redirect('read-list') #returns to the home page with the form
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
                    # Why does this need a context dictionary? YES, 
                    #ALSO should I reference a url or should I make a template and refence it with render... MAKE TEMPLATE and RENDER

def remove(request, id):
    item = Basic_crud_app.objects.get(id = id)
    item.delete()
    return redirect('read-list')

def update(request, id):
    item = Basic_crud_app.objects.get(id = id)
    # print(item)
    context ={
        'blurb': item
        }
    if request.method == 'GET':
        return render(request, 'pages/update.html', context)
    elif request.method == 'POST':
        item.message = request.POST['message']
        item.save()
        # item.description = request.POST['description']
        return redirect('read-list')

    


# TODO - add views and url paths to updates and removes 
# <a href="{% url 'update' todo.id %}">update</a>
# <a href="{% url 'remove' todo.id %}">remove</a>

# HTML from todos
# <a href="{% url 'update' todo.id %}">update</a>
# <a href="{% url 'remove' todo.id %}">remove</a>
# <a href="{% url 'read-list' %}">back to list</a>




