from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt

# the index function is called when root is visited

def index(request):
	return render(request, "helper/index.html")

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


		jobs = Job.objects.filter(assigned_to_id=request.session['id'])
		# Load all the jobs
		context = {
		 'all_jobs': Job.objects.filter(assigned_to_id=-99),
		 'my_jobs' : Job.objects.filter(assigned_to_id=request.session['id'])
		}


		print("COUNT: " + str(jobs.count()))
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

		# Load all the jobs
		context = {
		 'all_jobs': Job.objects.filter(assigned_to_id=-99),
		 'my_jobs' : Job.objects.filter(assigned_to_id=request.session['id'])
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


def mainjobs(request):
	context = {
		'user': User.objects.get(id = request.session['id']),
		'all_jobs': Job.objects.filter(assigned_to_id=-99),
		'my_jobs' : Job.objects.filter(assigned_to_id=request.session['id'])
	}		
	return render(request, "helper/dashboard.html", context)

def addjob(request):
	return render(request, "helper/addjob.html")

def viewjob(request, job_num):
	context = {
	  'job' : Job.objects.get(id=job_num)
	}

	return render(request, "helper/view.html", context)

def edit(request, job_num):
	context = {
	  'job' : Job.objects.get(id=job_num)
	}
	request.session['edit_job'] = job_num

	return render(request, "helper/edit.html", context)


def editjob(request):

	error = []

	print("editing job!")
	errors = Job.objects.validate_job(request.POST)

	# if there are no errors
	if (len(errors) == 0):
		# save the job
		job = Job.objects.get(id = request.session['edit_job'])
		job.title=request.POST['title'] 
		job.description=request.POST['description'] 
		job.location=request.POST['location']

		job.save()


		# Load all the quotes
		context = {
		  'all_jobs': Job.objects.filter(assigned_to_id=-99)
		}

		# redirect to the job dashboard
		return redirect("/dashboard", context)

	# if there are errors:
	else:
		# store in messages
		for e in errors:
			print(e) #print to the terminal
			messages.error(request, e)


		# redirect to the add job page
		return redirect("/edit/job_num")


def acceptjob(request, job_num):

	job = Job.objects.get(id=job_num)
	job.assigned_to_id = request.session['id']
	job.save()


	jobs = Job.objects.filter(assigned_to_id=request.session['id'])
	
	# Load all the jobs
	context = {
	  'all_jobs': Job.objects.filter(assigned_to_id=-99),
	  'my_jobs' : jobs
	}

	return redirect("/dashboard", context)

def completejob(request, job_num):

	job = Job.objects.get(id=job_num)
	job.completed_by_id = request.session['id']
	job.save()

	jobs = Job.objects.filter(assigned_to_id=request.session['id']).filter(completed_by_id=-99)
	
	# Load all the jobs
	context = {
	  'all_jobs': Job.objects.filter(assigned_to_id=-99),
	  'my_jobs' : jobs
	}

	return redirect("/dashboard", context)


def add(request):
	errors = []

	print("adding job!")
	errors = Job.objects.validate_job(request.POST)

	# if there are no errors
	if (len(errors) == 0):
		# save the job
		job = Job.objects.create(title=request.POST['title'], description=request.POST['description'], location=request.POST['location'], created_by_id=request.session['id'], assigned_to_id=-99, completed_by_id=-99)

		# Load all the quotes
		context = {
		  'all_jobs': Job.objects.filter(assigned_to_id=-99),
		  'my_jobs' : Job.objects.filter(assigned_to_id=request.session['id'])
		}

		# redirect to the job dashboard
		return redirect("/dashboard", context)

	# if there are errors:
	else:
		# store in messages
		for e in errors:
			print(e) #print to the terminal
			messages.error(request, e)


		# redirect to the add job page
		return redirect("/addJob")

def deletejob(request, job_num):

	job = Job.objects.get(id=job_num)

	job.delete() 

	context = {
	  'all_jobs': Job.objects.filter(assigned_to_id=-99),
	  'my_jobs' : Job.objects.filter(assigned_to_id=request.session['id'])
	}

	# redirect to the main job page
	return redirect("/dashboard", context)



