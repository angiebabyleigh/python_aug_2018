from django.db import models
import re

class UserManager(models.Manager):
	def checkuserinfo():
		error = []
		
		# validate first_name
		if ((length(first_name) < 2): #|| ( ! x.isalpha() for each x in first_name)):
			error.append("First Name required. No fewer than 2 characters; letters only")

		# validate last_name
		if ((length(last_name) < 2) || ( ! x.isalpha() for each x in last_name)):
			error.append("Last Name required. No fewer than 2 characters; letters only")

		# validate email
		if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
			error.append("Email required; Valid Format")

		# validate password
		if ((length(password) < 7) || (password != request.form.confirm)):
			error.append("Password required; No fewer than 8 characters in length; matches Password Confirmation")

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()