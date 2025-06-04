from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
from .models import User, Note
from django.contrib import messages
from django.contrib.auth.decorators import login_required



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

@login_required
def note_creation(request):
	if request.method=="POST":
		note_title = request.POST["note_title"]
		note_content = request.POST["note_content"]
		if Note.objects.filter(user=request.user, note_title=note_title):
			messages.error(request, 	"Note with same title exists already")
			return redirect("note_creation")
		else:
			new_note = Note(user=request.user, note_title=note_title, note_content=note_content)
			new_note.save()
		return redirect('note_creation')

	return render(request, "note_creation.html")

def note_list(request):
	notes = Note.objects.filter(user=request.user).order_by('-created_on')
	return render(request, 'note_list.html', {'notes': notes})


def note_detail(request, note_id):
	note = Note.objects.get(note_id=note_id, user=request.user)
	return render(request, 'note_detail.html', {'note': note})






			
