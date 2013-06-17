from django.db import models

# Create your models here.

class Task(models.Model):
	name = models.CharField(max_length=200)
	due_date = models.DateTimeField('due to date')
	done = models.BooleanField(default=False)

