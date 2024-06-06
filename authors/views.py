from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Authors, Questions, Post, Answers

# Create your views here.
@login_required(login_url='/authors/')
def authors_list(request):
	authors = Authors.objects.all()
	question = Questions.objects.all()
	post = Post.objects.all()
	answer = Answers.objects.all()

	context = {
		'title': 'Авторы',
		'authors': authors,
		'question': question,
		'post': post,
		'answer': answer
	}
	return render(request, 'authors/authors.html', context=context)