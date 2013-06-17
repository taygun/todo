from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=200)
	due_date = models.DateTimeField('due to date')
	done = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

class TaskForm(forms.Form):
	name = forms.CharField(max_length=200)
	due_date = forms.DateTimeField(required=False)

