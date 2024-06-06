from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import authors_list

urlpatterns = [
    path('', authors_list, name='authors_list'),
]
