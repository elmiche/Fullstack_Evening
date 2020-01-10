from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Todo  #importing the Todo class from models.py

# def home(request):
#   return HttpResponse('hello from the home view')

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/list.html', context) #this is the template path

def add_todo(request):
    if request.method == 'POST':  #needed to send form to the url todo/add
        title = request.POST['title'] #the 'name' of the labels/tags in add.html
        text = request.POST['text']
        if (request.POST['status'] == 'False'):
            status = False
        else:
            status = True
        Todo.objects.create( title = title, text = text, status = status)
        return render(request, 'todos/list.html') #this is the template path
    else: 
        return render(request, 'todos/add.html') #this is the template path


def details(request, id):
    todo = Todo.objects.get(id = id)
    return render(request, 'todos/detail.html', {"todo": todo})

def mark_done(request, id):
    # return HttpResponse('hello from the update view')
    todo = Todo.objects.get(id = id)
    todo.status = True
    todo.save()
    return redirect('details', todo.id)

def remove_todo(request, id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    return redirect('list')

def update_todo(request, id):
    todo = Todo.objects.get(id = id)
    print(request.POST['description'])
    return redirect('details', todo.id)  #details page

def update(request, id):
    todo = Todo.objects.get(id = id)
    if request.method == 'GET':
        return render(request, 'todos/update.html', {'todo': todo})
    elif request.method == 'POST':
        todo.title = request.POST['title']
        todo.text = request.POST['text']
        if (request.POST['status'] == 'False'):
            todo.status = False
        else:
            todo.status = True
        todo.save()
        return redirect('details', todo.id)
    return HttpResponse('hello from the update view')




