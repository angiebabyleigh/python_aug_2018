from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
	return render(request, "quoteme/index.html")


def login(request):
	user = User.objects.get(email_address=request.POST['email'])

	print(user.first_name)

	errors = User.objects.validate_login(request.POST)
	# if there are errors add to messages
	if len(errors) != 0:
		for e in errors:
			messages.error(request, e)
		# then redirect to the login page
		return redirect('/')
	# if there are no errors:
	else:
		# Get the correct user 
		user = User.objects.filter(email_address=request.POST['email'])
		request.session['id'] = user[0].id

		# Load all the quotes
		context = {
		'quotes': Quote.objects.all()
		}
		# q = Quote.objects.first()
		# if len(q.author) != 0:
		# 	print(q.author)
		# 	print(q.quote)
		# else:
		# user = User.objects.first()
		# print(user.first_name)
		# user.save()

		# redirect to the main quote page
		return redirect("/quotes", context)


def register(request):
	errors = User.objects.checkuserinfo(request.POST)
	# if there are no errors
	if (len(errors) == 0):
		# hash the password
		hashpw = bcrypt.hashpw(request.POST['passwd'].encode(), bcrypt.gensalt()).decode()
		
		# add the user to the db
		user = User.objects.create(first_name=request.POST['first'], last_name=request.POST['last'], email_address=request.POST['email'], password=hashpw)
		request.session['id'] = user.id

		# Load all the quotes
		context = {
		'quotes': Quote.objects.all()
		}

		# redirect to the main quote page
		return redirect("quotes", context)
	
	# if there are errors:
	else:
		# store in messages
		for e in errors:
			print(e) #print to the terminal
			messages.error(request, e)
		# redirect to login page	
		return redirect('/')

def logout(request):
	#clear session
	if 'id' in request.session:
		request.session.pop('id')

	# redirect to login page
	return redirect ('/')

def addquote(request):
	errors = []

	errors = Quote.objects.validate_quote(request.POST)

	# if there are no errors
	if (len(errors) == 0):
		# save the quote
		quote = Quote.objects.create(author=request.POST['author'], quote=request.POST['quote'], user_id=request.session['id'])

		# Load all the quotes
		context = {
		  'quotes': Quote.objects.all()
		}
	# if there are errors:
	else:
		# store in messages
		for e in errors:
			print(e) #print to the terminal
			messages.error(request, e)

	# redirect to the main quote page
	return redirect("/quotes", context)

def quotes(request):
	context = {
		'user': User.objects.get(id = request.session['id']),
		'quotes': Quote.objects.all()
	}
	return render(request, 'quoteme/quotes.html', context)


def userquotes(request, user_num):

	print(request.session['id'])
	context = {
		'user': User.objects.get(id = user_num),
		'quotes': Quote.objects.filter(user_id = user_num)
	}
	return render(request, 'quoteme/userquotes.html', context)


def like(request):
	print("user id = " + request.POST['user_id'])
	print("quote id = " + request.POST['quote_id'])

	errors = []

	errors = Likes.objects.checklikeinfo(request.POST)

	# if there are no errors
	if (len(errors) == 0):
		# save the like
		like = Likes.objects.create(user_id=request.POST['user_id'], quote_id=request.POST['quote_id'])

	# return to the quote page
	context = {
		'user': User.objects.get(id=request.session['id']),
		'quotes': Quote.objects.all()
	}

	return redirect("/quotes", context)


def edit(request, user_num):
	context = {
		'user': User.objects.get(id=user_num)
	}
	return render(request, 'quoteme/edit.html', context)

def update(request):

	errors = []

	errors = User.objects.checkuserinfo(request.POST)
	
	# if there are no errors
	if (len(errors) == 0):
		# save the user
		user = User.objects.update(first_name=request.POST['first'], last_name=request.POST['last'], email_address=request.POST['email'])

		# Load all the quotes
		context = {
		  'quotes': Quote.objects.all()
		}
	# if there are errors:
	else:
		# store in messages
		for e in errors:
			print(e) #print to the terminal
			messages.error(request, e)

		# redirect to the edit account page
		return redirect("/myaccount", context)



	# redirect to the main quote page
	return redirect("/quotes", context)





