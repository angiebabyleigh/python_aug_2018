from django.shortcuts import render, HttpResponse, redirect
def gold(request):
	response = "Go for the gold!!"
	return HttpResponse(response)
