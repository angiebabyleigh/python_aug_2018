from django.shortcuts import render, HttpResponse, redirect

def words(request):
	response = "Choose your words wisely!!"
	return HttpResponse(response)


def clear(request):
	response = "Clear this ____ out of here!!!"
	return HttpResponse(response)
