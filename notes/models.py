from django.db import models

# Create your models here.

import uuid
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	user_name = models.CharField(max_length=128)
	user_email = models.EmailField(max_length=128)
	password = models.CharField(max_length=128)
	last_update = models.DateField(auto_now=True)
	create_on = models.DateField(auto_now_add=True)


	def __str__(self):
		return (self.user_name)


class Note(models.Model):
	#many to one 
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

	note_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	note_title = models.CharField(max_length=128)
	note_content = models.CharField(max_length=400)
	last_update = models.DateField(auto_now=True)
	created_on = models.DateField(auto_now_add=True)

	def __str__(self):
		return (self.note_title)
