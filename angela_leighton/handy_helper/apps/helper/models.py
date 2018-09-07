from django.db import models
import re
import bcrypt
from django.conf import settings

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
class UserManager(models.Manager):
	def checkuserinfo(self, input):
		error = []
		
		# validate first_name
		if (len(input["first"]) < 2):
			error.append("First Name required. No fewer than 2 characters;")

		# validate last_name
		if (len(input["last"]) < 2):
			error.append("Last Name required. No fewer than 2 characters;")

		# validate email
		if not EMAIL_REGEX.match(input['email']):
			error.append("Invalid email format")

		# validate password
		if (len(input["passwd"]) < 7): 
			error.append("Password required; No fewer than 8 characters in length")

		if (input["passwd"] != input["confirm"]):
			error.append("Password must match Password Confirmation")

		return error

	def validate_login(self, input):
		error = []

		# look for the user
		user = User.objects.filter(email_address=input['email'])
		
		# if the user does not exist give an error message
		if len(user) == 0:
			error.append("Email does not exist")
			return error

		# if you find the user make sure the password is correct	
		if bcrypt.checkpw(input['passwd'].encode(), user[0].password.encode()):
			print("passwords match")
		else:
			error.append("Password is incorrect")  
		
		return error

class JobManager(models.Manager):
	def validate_job(self, input):
		error = []

		# validate title
		if (len(input["title"]) < 4):
			error.append("Title is required. Must be greater than 3 characters;")

		# validate description
		if (len(input["description"]) < 11):
			error.append("Description is required. Must be greater than 10 characters;")

		# validate location
		if (len(input["location"]) < 1):
			error.append("Location is required;")

		return error


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()

class Job(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	location = models.CharField(max_length=255)
	created_by = models.ForeignKey(User, related_name="requests", on_delete = models.CASCADE)
	assigned_to = models.ForeignKey(User, related_name="jobs", on_delete = models.CASCADE)
	completed_by = models.ForeignKey(User, related_name="completed", on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = JobManager()




