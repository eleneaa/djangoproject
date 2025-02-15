from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from.models import Task
from django.utils import timezone
from django.views.generic.dates import timezone_today

def today_tasks(request):

    tasks =Task.objects.all()
    return render(request,'templates/taask.html',{'tasks':tasks})