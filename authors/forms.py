from django import forms
from django.contrib.auth import authenticate, get_user_model
from .models import Authors, Questions, Post

class CreatePost(forms):
	pass