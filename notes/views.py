from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
from .models import User
from django.contrib import messages



def register(request):
	if request.method=="POST":
		username = request.POST["user_name"]
		email = request.POST["user_email"]
		password = request.POST["password"]
		if User.objects.filter(user_email=email):
			messages.error(request, "Email already exists")
			return redirect('register')
		else:
			new_user = User(user_name=username, user_email=email, password=password)
			new_user.save()
			messages.success(request, 'Registration successful. Please log in.')
			return redirect('login')
	return render(request, 'register.html')

def login(request):
	if request.method=="POST":
		email = request.POST["user_email"]
		password = request.POST["password"]
		try:
			User.objects.get(user_email=email)
			if (password == password):
				return redirect('register')
			else:
				messages.error(request, "Please check your email and password.")
		except User.DoesNotExist:
			messages.error(request, "User not found")

	return render(request, "login.html")


# def notes_creation(request):






			
