from django.shortcuts import render, redirect
from .models import Todo
from .form import TodoForm


# Create your views here.
def homepage(request):
    # todos = Todo.objects.all()

    if request.method == "POST":
        todo_form = TodoForm(request.POST)
        # todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            todo = todo_form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('homepage')
        else:
            print("form not valid")

    else:
        todo_form = TodoForm()

    context = {
        'todos': Todo.objects.all(),
        'todo_form': todo_form,
    }
    
    return render(request, 'homepage.html', context)


def delete_todo(request,pk):
    todo = Todo.objects.get(id = pk)
    todo.delete()
    return redirect('homepage')
