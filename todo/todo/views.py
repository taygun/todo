from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect,render
from django.contrib.auth import authenticate, login
from todo.models import Task


def index(request):
	Tasks = Task.objects.all()	
	return render(request, 'mytodolist.html', {'Tasks' : Tasks})	
	

