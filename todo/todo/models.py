from django.db import models
from django import forms

# Create your models here.

class Task(models.Model):
	name = models.CharField(max_length=200)
	due_date = models.DateTimeField('due to date')
	done = models.BooleanField(default=False)

class TaskForm(forms.Form):
	name = forms.CharField(max_length=200)
	due_date = forms.DateTimeField(required=False)
