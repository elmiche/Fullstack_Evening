from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Todo

def todo_list(request):
    return HttpResponse('hello from the todo_list view')

def details(request, id):
    return HttpResponse('hello from the details view')

def add_todo(request):
    return HttpResponse('hello from the add_todo view')

def remove_todo(request, id):
    return HttpResponse('hello from the remove view')

def update_todo(request, id):
    return HttpResponse('hello from the update_todo view')

def update(request, id):
    return HttpResponse('hello from the update view')



