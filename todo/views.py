from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST
# Create your views here.
def index(request):
    todo_list = Todo.objects.filter(user_id = request.user.id)
    form = TodoForm()
    context = {
        'todo_list': todo_list,
        'form': form,
    }
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        data = request.POST['text']
        new_todo = Todo(text = data, user_id = request.user)
        new_todo.save()
    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete=True).delete()
    return redirect('index')
def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')