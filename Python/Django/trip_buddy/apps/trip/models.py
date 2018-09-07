from django.db import models
import re
import bcrypt
from django.conf import settings
from datetime import datetime, date

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
		if (len(input["passwd"]) < 8): 
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

class TripManager(models.Manager):
	def validate_trip(self, input):
		error = []

		print(input['destination'])
		print(input['description'])
		print(input['startdate'])
		print(input['enddate'])

		# validate destination
		if (len(input["destination"]) < 1):
			error.append("Destination is required;")

		# validate description
		if (len(input["description"]) < 1):
			error.append("Description is required;")

		
		# # d1 = dateutil.parser.parse(input["startdate"]).date()
		# # d1 = datetime.strptime(input["startdate"], '%m/%d/%Y')
		# d1 = date_converter.string_to_date(input["startdate"], '%Y-%m-%d %H:%M:%S')

		# # now = datetime.strptime(date.today(), '%m/%d/%Y').strftime('%F %T')
		# # now = dateutil.parser.parse(date.today()).date()
		# now = date_converter.string_to_date(date.today(), '%Y-%m-%d %H:%M:%S')

		# # validate start_date
		# if (d1 < now):
		# 	error.append("Trip must begin in the future;")
		
		# # d2 = dateutil.parser.parse(input["enddate"]).date()
		# # d2 = datetime.strptime(input["enddate"], '%m/%d/%Y').strftime('%F %T')
		# d2 = date_converter.string_to_date(input["enddate"], '%Y-%m-%d %H:%M:%S')

		# # validate end_date
		# if (d2 < d1):
		# 	error.append("Trip must end after it begins;")

		return error


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()


class Travel(models.Model):
	destination = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	planned_by = models.ForeignKey(User, related_name="planned_trips", on_delete = models.CASCADE)
	user = models.ManyToManyField(User, related_name="my_trips")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = TripManager()


