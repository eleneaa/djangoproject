from django.db import models
from django.template.defaultfilters import title


class Task(models.Model):
    title= models.CharField(unique=True, max_length=200,verbose_name='название задачи')
    description = models.TextField(blank=True, null=True, help_text='описание задачи',verbose_name='описание задачи')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Дата создания')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title



