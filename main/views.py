from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TodoForm
from .models import Todo, TodoItems


# Create your views here.


def home(request):
    todos = Todo.objects.all()

    # massage = '''hela from django'''
    # return HttpResponse(massage)
    context = {
        # "message": massage
        "todos": todos,
    }
    return render(request, 'home.html', context)


def detailed(request, id):
    todo = Todo.objects.get(id=id)
    items = todo.todoitems_set.all()
    context = {
        "todo": todo,
        "items": items
    }
    return render(request, 'detailed.html', context)


def createTodo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form": form

    }
    return render(request, 'create.html', context)


def updateTodo(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form": form

    }
    return render(request, 'update.html', context)


def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')
