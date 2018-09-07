# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
  

def word(request):
	if 'attempts' not in request.session:
		request.session["attempts"] = 0
	else:
		request.session["attempts"] += 1

	context = {
		'random' : get_random_string(length=14),
	}

	return render(request, "apps/word/index.html", context)

def reset(request):
	request.session['attempts'] = 0
	return redirect('word')