import os
import datetime
from django.db import models
from django.urls import reverse


class Authors(models.Model):
    def make_photo_autors(instance, filename):
        path = 'authors/%s'
        return path

    class Meta:
        verbose_name = 'Публицист'
        verbose_name_plural = 'Публицисты'
        ordering = ['-birthday']

    surname = models.CharField(verbose_name="Фамилия", max_length=50)
    name = models.CharField(verbose_name="Имя", max_length=50, blank=True)
    middlename = models.CharField(verbose_name='Отчества', max_length=50, blank=True)
    birthday = models.DateField(verbose_name="Дата рождения", default=datetime.date.today)
    birthplace = models.CharField(verbose_name="Место рождения", max_length=200, blank=True)
    deathday = models.DateField(verbose_name="Дата смерти", blank=True, null=True, default=None)
    deathlace = models.CharField(verbose_name="Место смерти", max_length=200, blank=True, null=True, default=None)
    description = models.TextField(verbose_name="Краткое описание", blank=True)
    logo = models.ImageField(verbose_name='Аватарка', blank=True, null=True, upload_to = 'authors/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Время изменения')

    def __str__(self):
        return self.name

    def age(birthdate):
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def get_full_name(self):
        if self.surname:
            if self.middlename:
                return self.surname + ' ' + self.name + ' ' + self.middlename
            return self.surname + ' ' + self.name
        return self.name

class Questions(models.Model):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    question = models.CharField(verbose_name="Вопрос", max_length=350)

    def __str__(self):
        return self.question

class Answers(models.Model):
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    answer = models.CharField(verbose_name="Ответ", max_length=250)
    question = models.ForeignKey('Questions', on_delete=models.PROTECT, null=True, verbose_name='Вопрос')
    author = models.ForeignKey('Authors', on_delete=models.PROTECT, null=True, verbose_name='Публицист')

    def __str__(self):
        return self.answer

class Post(models.Model):
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    title = models.CharField(verbose_name = "Заголовок", max_length=100)
    description = models.TextField(verbose_name = "Запись", max_length=600)

    def __str__(self):
        return self.title

# class Comments(models.Model):
#     class Meta:
#         verbose_name = 'Комментарий'
#         verbose_name_plural = 'Комментарии'

#     mention_text = models.TextField()
#     mention_digit = models.IntegerField()

#     def get_star(self):
#         if self.mention_digit == 1:
#             return 'class="fa fa-star"'*1 and 'class="fa fa-star-o"'*4
#         elif self.mention_digit == 2:
#             return 'class="fa fa-star"'*2 and 'class="fa fa-star-o"'*3
#         elif self.mention_digit == 3:
#             return 'class="fa fa-star"'*3 and 'class="fa fa-star-o"'*2
#         elif self.mention_digit == 4:
#             return 'class="fa fa-star"'*4 and 'class="fa fa-star-o"'*1
#         elif self.mention_digit == 5:
#             return 'class="fa fa-star"'*5 and 'class="fa fa-star-o"'*0
#         else:
#             return self.mention_digit

         # fa-star