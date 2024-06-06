from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from .views import my_profile, settings, password_change, password_change_done


urlpatterns = [
    path('', my_profile, name='my_profile'),
    path('edit/', settings, name='settings'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name = 'profiles/user_password_change.html', success_url=reverse_lazy('admin:index'),), name='password_change'),
    # path('password-change/done/', password_change_done, name='password_change_done'),
    path('password-change/', password_change, name='password_change'),
    # path('password-change/done/', auth_views.password_change_done.as_view(name='password_change_done.html'), name='password_change_done'),
]
