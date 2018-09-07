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

class QuoteManager(models.Manager):
	def checkquoteinfo(self, input):
		error = []

		# validate author
		if (len(input["author"]) < 3):
			error.append("Author is required. No fewer than 3 characters;")

		# validate quote
		if (len(input["quote"]) < 10):
			error.append("Quote is required. No fewer than 10 characters;")

		return error

class LikeManager(models.Manager):
	def checklikeinfo(self, input):

		error = []
		
		# look for the like
		like = Likes.objects.filter(quote_id=input['quote_id'], user_id=input['user_id'])
		
		# if the like does not exist give an error message
		if len(like) != 0:
			error.append("You have already liked this quote!")
		
		return error


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()


class Quote(models.Model):
	author = models.CharField(max_length=255)
	quote = models.TextField()
	user = models.ForeignKey(User, related_name="quotes", on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = QuoteManager()

class Likes(models.Model):
	user = models.ForeignKey(User, related_name="likes", on_delete = models.CASCADE)
	quote = models.ForeignKey(Quote, related_name="likes", on_delete = models.CASCADE)

	objects = LikeManager()






