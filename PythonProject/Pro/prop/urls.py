from django.contrib import admin
from django.urls import path, include


from .views import *

urlpatterns = [
    path('',hello,name='hello'),
    path('all_task/',all_tasks,name='tasklist'),
    path('today_tasks/',today_tasks,name='today_tasks'),
    path('add-task/',add_task,name='add_task'),
    path('task-added/<str:title>/',task_added,name='task_added'),
    path('task-edit/<str:title>/',editTask,name='task_edit'),
    path('task-edited/<str:title>/',task_edited,name='task_edited')
]

