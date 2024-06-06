from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Questions, Answers, CommentUser, RatingAnswer, RatingComment
from profiles.models import Profile
from .forms import QuestionForm, AnswersForm

@login_required(login_url='/questions/')
def question_list(request):
	question = Questions.objects.all()
	answer = Answers.objects.all()
	comment_user = CommentUser.objects.all()
	rating_answer = RatingAnswer.objects.all()
	rating_comment = RatingComment.objects.all()

	context = {
		'title': 'Вопросы',
		'question': question,
		'answer': answer,
		'comment_user': comment_user,
		'rating_answer': rating_answer,
		'rating_comment': rating_comment,
	}
	return render(request, 'questions/questions.html', context=context)

@login_required(login_url='/questions/')
def question_added(request):
	if request.method == "POST":
		form = QuestionForm(request.POST)
		if form.is_valid():
			new_question = form.save()
			new_question.name = request.POST.get("name")
			messages.success(request, 'Вопрос создан')
	else:
		form = QuestionForm()

	context = {
		'title': 'Создать вопрос',
		'form': form,
	}

	return render(request, 'questions/question_add.html', context=context)

@login_required(login_url='/questions/')
def get_question(request, quest_id):
	question = Questions.objects.filter(quest_id = questions_id)
	answer = Answers.objects.get(fk = questions_id)

	context = {
		'title': '<int:questions_id>',
		'question': question,
		'answer': answer, 
	}

	return render(request, 'questions/question_quest.html', context=context)

@login_required(login_url='/answer/')
def get_question(request):
	answer = Answers.objects.get(pk=answer_id)

	context = {
		'title': '<int:answer_id>',
		'answer': answer, 
	}

	return render(request, 'questions/question_quest.html', context=context)



@login_required(login_url='/questions/')
def answer_added(request):
	form = AnswersForm()

	context = {
		'title': 'Создать ответ',
		'form': form,
	}
	return render(request, 'questions/answer_add.html', context=context)