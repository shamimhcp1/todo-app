from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from . models import Todo

# Create your views here.
def index(request):
    context = {'todo_list' : Todo.objects.all().order_by('-id').values()}
    return render(request, 'todoapp/todo_list.html', context)

def add_todo(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todo/')


def update_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.content = request.POST['content']
    todo.save()
    return redirect('/todo/')

def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if todo.complete == False:
        todo.complete = True
    else:
        todo.complete = False
    todo.save()
    return redirect('/todo/')


def delete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('/todo/')

def edit_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    return render(request, 'todoapp/todo_edit.html', {'todo': todo})