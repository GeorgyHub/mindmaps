from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import question_list, question_added, get_question, answer_added

urlpatterns = [
	path('', question_list, name='question_list'),
	path('add_question', question_added, name='question_added'),
	path('question/<int:questions_id>', get_question, name='Question'),
	path('answer_added', answer_added, name='answer_added'),
]