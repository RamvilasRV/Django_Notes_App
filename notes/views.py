from django.shortcuts import render

# Create your views here.
from .models import User
from django.contrib import messages



def register(request):
	if request.method=="POST":
		username = request.POST["username"]
		email = request.POST["email"]
		password = request.POST["password"]
		if User.Object.filter(user_email=email):
			messages.error(request, "Email already exists")
		else:
			new_user = User(user_name=username, user_email=email, password=password)
			new_user.save()
			
