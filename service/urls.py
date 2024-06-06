from django.urls import path, re_path
from .views import index, sing_up, user_login, user_logout
from profiles.forms import UserRegistrationForm

urlpatterns = [
    path('', index, name='index'),
    path('sing_in/', user_login, name='login'),
    path('sing_up/', sing_up, name='sing_up'),
    path('logout/', user_logout, name='user_logout'),
]