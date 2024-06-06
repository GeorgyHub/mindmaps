from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from .forms import UserEditForm

# from somewhere import handle_uploaded_file

# Create your views here.
@login_required(login_url='/sing_in/')
def my_profile(request):
	return render(request, 'profiles/mypage.html')

@login_required(login_url='/sing_in/')
def settings(request):
	user = User.objects.get(pk=request.user.pk)
	profile = User.profile
	form = UserEditForm(instance = request.user.profile)

	if request.method == "POST":
		form = UserEditForm(request.POST, request.FILES, instance = request.user.profile)

		if form.is_valid():
			update = form.save(commit=False)
			update.save()
			message = form.cleaned_data['name']

	context = {
		'form': form
	}

	return render(request, 'profiles/settings.html', context=context)

@login_required(login_url='/sing_in/')
def password_change(request):
	if request.method == "POST":
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			update = form.save(commit=False)
			update.save()
			update_session_auth_hash(request, request.user)

			return redirect('profiles:settings')

		context = {
			'form': form
		}
		return render(request, 'profiles/user_password_change.html', context=context)

	form = PasswordChangeForm(user = request.user)
	context = {
		'form': form
	}
	return render(request, 'profiles/user_password_change.html', context=context)


def password_change_done(request):
	form = User


	return render(request, 'profiles/user_password_change.html')

