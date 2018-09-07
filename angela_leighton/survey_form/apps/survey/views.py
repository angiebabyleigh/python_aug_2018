from django.shortcuts import render, HttpResponse, redirect

def survey(request):
	# response = "Hello, I am your first survey!"
	return render(request, "app/survey/index.html")
