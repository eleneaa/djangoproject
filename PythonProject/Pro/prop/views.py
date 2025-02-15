from gc import get_objects

from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from .models import Task

def today_tasks(request):
    today=timezone.now().date()
    tasks=Task.objects.filter(created_at__date=today)
    upt_task = Task.objects.filter(updated_at__date=today)
    tasks = tasks.union(upt_task)
    return render(request,'today_tasks.html',{'tasks':tasks})

def all_tasks(request):
    today=timezone.now().date()
    tasks=Task.objects.all()
    return render(request,'all_task.html',{'tasks':tasks})

def hello(request):
    return render(request, 'base.html')

def task_added(request,title):
    return render(request,'task_added.html',{'title':title})

def add_task(request):
    if request.method =='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_added',title=form.cleaned_data['title'])
    else:
        form = TaskForm()

        return render(request,'add_task.html',{'form':form})


def editTask(request, title):
    task = get_object_or_404(Task, title=title)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            # Сохранение формы
            updated_task = form.save(commit=False)
            updated_task.updated_at = timezone.now()  # Обновление времени
            updated_task.save()  # Сохранение задачи

            return redirect('task_edited', title=form.cleaned_data['title'])

    else:
        form = TaskForm(instance=task)  # Если это GET-запрос, то инициализируем форму с существующей задачей

    return render(request, 'Edit_task.html', {'form': form})


def task_edited(request,title):
    return render(request,'task_edited.html',{'title':title})


