from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect,render
from django.contrib.auth import authenticate, login



def index(request):
	return render(request, 'mytodolist.html', {'todo' : 'nimic'})	
	

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			state = "Logged in"
			return redirect('http://google.ro')
				
		else:
			state = "Not active"
	else:
		state = "Your username/password was incorrect"
	return render_to_response('login.html',
			{'state':state,
			'username':username,
			},
			context_instance=RequestContext(request)
			)	
