import datetime
from django.db import models
from django.contrib.auth.models import User

class Questions(models.Model):
	user_quest = models.ForeignKey(User, on_delete = models.PROTECT, null=True, verbose_name = 'Вопрос пользователя')
	name = models.CharField(max_length = 150, verbose_name = 'Вопрос')
	created_at = models.DateTimeField(verbose_name = 'Дата создание вопроса', default=datetime.datetime.now())

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'
		ordering = ['name']

	def __str__(self):
		return self.name

class CommentUser(models.Model):
	class Meta:
		verbose_name = 'Комментарий пользователя'
		verbose_name_plural = 'Комментарии пользователя'
		ordering = ['text']

	User = models.ForeignKey(User, on_delete = models.PROTECT, null=True, verbose_name = 'Пользователь')
	text = models.TextField(blank = True, verbose_name = 'Описание комментария')

	def __str__(self):
		return self.text

class Answers(models.Model):
	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'
		ordering = ['title']

	user = models.ForeignKey(User, on_delete = models.PROTECT, null=True, verbose_name = 'Вопрос пользователя')
	title = models.CharField(max_length = 100, verbose_name = 'Ответ')
	text = models.TextField(max_length = 400, null = True, verbose_name = 'Описание')
	question = models.ForeignKey('Questions', on_delete = models.PROTECT, null = True, blank = True, verbose_name = 'Вопрос')
	comment = models.ForeignKey('CommentUser', on_delete = models.PROTECT, null = True, blank = True, verbose_name = 'Комментарий')
	rating = models.ForeignKey('RatingAnswer', on_delete = models.PROTECT, null = True, blank = True, verbose_name = 'Рейтинг')

	def __str__(self):
		return self.title

class RatingAnswer(models.Model):
	class Meta:
		verbose_name = 'Рейтинг ответа'
		verbose_name_plural = 'Рейтинги ответов'
		ordering = ['answer']

	user = models.ForeignKey(User, on_delete = models.PROTECT, null=True, verbose_name = 'Вопрос пользователя')
	answer = models.ForeignKey('Answers', on_delete = models.PROTECT, blank = True, verbose_name = 'Комментарий')
	rating_digit = models.IntegerField()

	def get_star(self):
		if self.rating_digit == 1:
			return '<i class="fa fa-star"></i>'*1
		elif self.rating_digit == 2:
			return '<i class="fa fa-star"></i>'*2
		elif self.rating_digit == 3:
			return '<i class="fa fa-star"></i>'*3
		elif self.rating_digit == 4:
			return '<i class="fa fa-star"></i>'*4
		elif self.rating_digit == 5:
			return '<i class="fa fa-star"></i>'*5
		else:
			return self.rating_digit

	def __str__(self):
		return str(self.rating_digit)

class RatingComment(models.Model):
	class Meta:
		verbose_name = 'Рейтинг комментария'
		verbose_name_plural = 'Рейтинги комментариев'
		ordering = ['comment']

	user = models.ForeignKey(User, on_delete = models.PROTECT, null=True, verbose_name = 'Вопрос пользователя')
	comment = models.ForeignKey('CommentUser', on_delete = models.PROTECT, null = True, verbose_name = 'Комментарий')
	rating_digit = models.IntegerField()

	def get_star(self):
		if self.rating_digit == 1:
			return '<i class="fa fa-star"></i>'*1
		elif self.rating_digit == 2:
			return '<i class="fa fa-star"></i>'*2
		elif self.rating_digit == 3:
			return '<i class="fa fa-star"></i>'*3
		elif self.rating_digit == 4:
			return '<i class="fa fa-star"></i>'*4
		elif self.rating_digit == 5:
			return '<i class="fa fa-star"></i>'*5
		else:
			return self.rating_digit

	def __str__(self):
		return str(self.rating_digit)