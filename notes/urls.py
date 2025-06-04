
from django.urls import path
from . import views

urlpatterns = [
	path("register/", views.register, name="register"),
	path("login/", views.login, name="login"),
	path("note_creation/", views.note_creation, name="note_creation"),
	path("note_list/", views.note_list, name="note_list"),
	path("note_detail/<uuid:note_id>", views.note_detail, name="note_detail")
]