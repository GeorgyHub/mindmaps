from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect
from django.contrib import messages
from profiles.forms import UserRegistrationForm, UserCreationForm, UserLoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from questions.models import Questions, CommentUser, Answers, RatingAnswer, RatingComment

def index(request, pk=None):
    question = None
    if pk:
        question = Questions.objects.filter(pk=pk).first()
        if not question:
            return redirect("Answers")
    if question:
        answer = Answers.objects.filter(question=question)
    else:
        answer = Answers.objects.all()

    context = {
        'title': 'Главная',
        'pk': pk,
        'questions': Questions.objects.all(),
        'answers': Answers.objects.filter(question=question),
        'comment_user': CommentUser.objects.all(),
        'rating_answer': RatingAnswer.objects.all(),
        'rating_comment': RatingComment.objects.all()
    }
    return render(request, 'index.html', context=context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()

    context = {
        'title': 'авторизация',
        'form': form,
    }

    return render(request, 'login.html', context=context)

def sing_up(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.profile.surname = request.POST['surname']
            new_user.profile.name = request.POST['name']
            new_user.profile.middlename = request.POST['middlename']
            new_user.profile.save()


            messages.success(request, 'Регистрация прошла успешно')
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
        'title': 'регистрация'
    }
    return render(request, 'register.html', context=context)

def user_logout(request):
    logout(request)
    return redirect('login')
