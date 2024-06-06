from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User as UserModel
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Profile

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
	username = forms.CharField(label = '', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'false', 'placeholder': 'Введите имя пользователя*'}), required=True)
	name  = forms.CharField(label = '', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'false', 'placeholder': 'Ваше имя*'}), required=True)
	middlename  = forms.CharField(label = '', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'false', 'placeholder': 'Ваше отчество'}), required=False)
	surname = forms.CharField(label = '', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'false', 'placeholder': 'Ваша фамилия*'}), required=True)
	password1 = forms.CharField(label = '', widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete':'false', 'placeholder': 'Задайте пароль*'}), required=True)
	password2 = forms.CharField(label = '', widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete':'false', 'placeholder': 'Повторите пароль*'}), required=True)

	def __init__(self, *args, **kwargs):
		super(UserRegistrationForm, self).__init__(*args, **kwargs)


	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', )


	def clean(self):
		data = self.cleaned_data
		username = data.get('username').lower()

		try:
			vaild_user = UserModel.objects.get(username=username)
		except UserModel.DoesNotExist:
			if username and UserModel.objects.filter(username=username).count()>0:
				raise forms.ValidationError('Используйте другое имя пользователя!')

			data['username'] = data['username'].lower()
			return data

		raise forms.ValidationError('Пользователь с таким именем существует!')

class UserLoginForm(AuthenticationForm):
	username = forms.CharField(label = '', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'false', 'placeholder': 'Введите имя пользователя*'}), required=True)
	password = forms.CharField(label = '', widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete':'false', 'placeholder': 'Задайте пароль*'}), required=True)

class UserEditForm(ModelForm):

	class Meta:
		model = Profile
		fields = ["surname", "name", "middlename", "logo", ]

	def __init__(self, *args, **kwargs):
		super(UserEditForm, self).__init__(*args, **kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

# class UserPasswordChangeForm(SetPasswordForm):
# 	class Meta:
# 		model = UserModel
# 		fields = ["password"]
#         # exclude = ('groups', 'user_permissions', 'is_staff')

# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
		
# 		for field in self.fields:
# 			self.fields[field].widget.attrs['class'] = 'form-control'

