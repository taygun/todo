from django.contrib import admin
from todo.models import Task


class TaskAdmin(admin.ModelAdmin):
	pass
admin.site.register(Task, TaskAdmin)
