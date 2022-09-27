from django.shortcuts import render
from todo.models import Todo
from .models import User
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from django.http import Http404

# Create your views here.
def todolist(request):
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render(request, 'todo/simpleTodo.html',
                          {'todolist': todolist,
                           'finishtodos': finishtodos})

def addTodo(request):
    if request.method == 'POST':
        atodo = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id='1')
        todo = Todo(user=user, todo=atodo, priority=priority, flag='1')
        todo.save()
        todolist = Todo.objects.filter(flag='1')
        finishtodos = Todo.objects.filter(flag=0)
        return render(request, 'todo/simpleTodo.html',
                              {'todolist': todolist, 
                               'finishtodos': finishtodos})
    else:
        todolist = Todo.objects.filter(flag=1)
        finishtodos = Todo.objects.filter(flag=0)
        return render(request, 'todo/simpleTodo.html',
                              {'todolist': todolist, 
                               'finishtodos': finishtodos})

def todofinish(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.flag == '1':
        todo.flag = '0'
        todo.save()
        return HttpResponseRedirect('/todos/')
    todolist = Todo.objects.filter(flag=1)
    return render(request, 'todo/simpleTodo.html',
                           {'todolist': todolist})

def todoback(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.flag == '0':
        todo.flag = '1'
        todo.save()
        return HttpResponseRedirect('/todos/')
    todolist = Todo.objects.filter(flag=1)
    return render(request, 'todo/simpleTodo.html', {'todolist': todolist})

def tododelete(request, id=''):
    try:
        todo = Todo.objects.get(id=id)
    except Exception:
        raise Response(status=404)
    if todo:
        todo.delete()
        return HttpResponseRedirect('/')
    todolist = Todo.objects.filter(flag=1)
    return render(request, 'todo/simpleTodo.html', {'todolist': todolist})
def updatetodo(request, id=''):
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(id=id)
        except Exception:
            return HttpResponseRedirect('/todos/')
        atodo = request.POST['todo']
        priority = request.POST['priority']
        todo.todo = atodo
        todo.priority = priority
        todo.save()
        return HttpResponseRedirect('/todos/')
    else:
        try:
            todo = Todo.objects.get(id=id)
        except Exception:
            raise Http404
        return render(request, 'todo/updatetodo.html', {'todo': todo})