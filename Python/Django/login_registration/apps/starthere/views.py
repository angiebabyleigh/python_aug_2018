from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def start(request):
	
	return render(request, "starthere/index.html")