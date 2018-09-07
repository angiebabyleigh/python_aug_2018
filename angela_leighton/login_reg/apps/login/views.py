from django.shortcuts import render
from .models import *
from django.contrib import messages


def home(request):
	return render(request, 'login/index.html')

def register(request):
	errors = User.objects.checkuserinfo(request.POST)
	if len(errors) == 0:
		hashpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt)

def login(request):
	errors = User.objects.validation_login(request)

	if len(errors) != 0:
		return redirect('/')
	else:
		return redirect('/success')

