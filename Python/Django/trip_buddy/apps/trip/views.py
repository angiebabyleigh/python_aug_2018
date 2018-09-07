from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
	return render(request, "trip/index.html")

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

		# Load the trips	
		# Load the trips	
		context = {
			'user': user,
			'other_trips' : Travel.objects.all()
		}


		# print("COUNT: " + str(jobs.count()))
		return redirect("/dashboard", context)


def register(request):
	errors = User.objects.checkuserinfo(request.POST)
	# if there are no errors
	if (len(errors) == 0):
		# hash the password
		hashpw = bcrypt.hashpw(request.POST['passwd'].encode(), bcrypt.gensalt()).decode()
		
		# add the user to the db
		user = User.objects.create(first_name=request.POST['first'], last_name=request.POST['last'], email_address=request.POST['email'], password=hashpw)
		request.session['id'] = user.id

		# Load the trips	
		context = {
			'user': user,
			'other_trips' : Travel.objects.all()
		}

		# redirect to the main job page
		return redirect("/dashboard", context)
	
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


def maintravels(request):
	user = User.objects.get(id = request.session['id'])
	context = {
		'user': user,
		'other_trips' : Travel.objects.all()
	}		
	return render(request, "trip/dashboard.html", context)

def add(request):
	return render(request, "trip/addtrip.html")

def addTrip(request):
	
	errors = Travel.objects.validate_trip(request.POST)

	# if there are no errors
	if (len(errors) == 0):
		
		# add the trip to the db
		trip = Travel.objects.create(
			destination=request.POST['destination'],
			description=request.POST['description'],
			start_date=request.POST['startdate'],
			end_date=request.POST['enddate'],
			planned_by_id=request.session['id'])

		user = User.objects.get(id=request.session['id'])


		user.my_trips.add(trip)

		# Load all the trips
		context = {
		 'user' : user,
		 'other_trips' : Travel.objects.all(),
		}


		# redirect to the main trip page
		return redirect("/dashboard", context)
	
	# if there are errors:
	else:
		# store in messages
		for e in errors:
			print(e) #print to the terminal
			messages.error(request, e)
		# redirect to add page	
		return redirect('/add')

def viewTrip(request, trip_num):
	trip = Travel.objects.get(id=trip_num)


	travelers = trip.user.all()

	context = {
		'trip' : trip,
		'travelers' : travelers
	}
	return render(request, "trip/view.html", context)



def joinTrip(request, trip_num):
	trip = Travel.objects.get(id=trip_num)
	user = User.objects.get(id=request.session['id'])

	user.my_trips.add(trip)

	context = {
	 'user' : user,
	 'other_trips' : Travel.objects.all(),
	 'my_trips': user.my_trips.all()
	}

	# redirect to the main trip page
	return redirect("/dashboard", context)


def cancelTrip(request, trip_num, user_num):
	trip = Travel.objects.get(id=trip_num)
	user = User.objects.get(id=user_num)

	user.my_trips.add(trip)
	user.my_trips.remove(trip)

	context = {
	 'user' : user,
	 'other_trips' : Travel.objects.all(),
	 'my_trips': user.my_trips.all()
	}

	# redirect to the main trip page
	return redirect("/dashboard", context)

def deleteTrip(request, trip_num):
	trip = Travel.objects.get(id=trip_num)
	trip.delete()
	user = User.objects.get(id=request.session['id'])

	context = {
	 'user' : user,
	 'other_trips' : Travel.objects.all(),
	 'my_trips': user.my_trips.all()
	}

	# redirect to the main trip page
	return redirect("/dashboard", context)









