# import os
# import datetime
# from django.db import models
# from django.urls import reverse
# from mptt.models import MPTTModel, TreeForeignKey

# class Authors(models.Model):
#     def make_photo_autors(instance, filename):
#         path = 'authors/%s'
#         return path

#     class Meta:
#         verbose_name = 'Публицист'
#         verbose_name_plural = 'Публицисты'
#         ordering = ['-birthday']

#     surname = models.CharField(verbose_name="Фамилия", max_length=50)
#     name = models.CharField(verbose_name="Имя", max_length=50, blank=True)
#     middlename = models.CharField(verbose_name='Отчества', max_length=50, blank=True)
#     birthday = models.DateField(verbose_name="Дата рождения", default=datetime.date.today)
#     birthplace = models.CharField(verbose_name="Место рождения", max_length=200, blank=True)
#     deathday = models.DateField(verbose_name="Дата смерти", blank=True)
#     deathlace = models.CharField(verbose_name="Место смерти", max_length=200, blank=True)
#     description = models.TextField(verbose_name="Краткое описание", blank=True)
#     logo = models.ImageField(verbose_name='Аватарка', blank=True, null=True, upload_to = 'authors/')
#     slug = models.SlugField(null=True)

#     def get_absolute_url(self):
#         return reverse("authors_detail", kwargs={'slug': self.slug})

#     def __str__(self):
#         return self.name

# class Post(models.Model):
#     class Meta:
#         verbose_name = 'Запись'
#         verbose_name_plural = 'Записи'

#     title = models.CharField(max_length=100, verbose_name='Заголовок')
#     slug = models.SlugField(max_length=150)
#     content = models.TextField(verbose_name='Описание')

#     def __str__(self):
#         return self.title

# class Questions(MPTTModel):
#     class Meta:
#         verbose_name = 'Вопрос'
#         verbose_name_plural = 'Вопросы'

#     class MPTTMeta:
#         order_insertion_by = ['title']

#     title = models.CharField(max_length=150)
#     parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', db_index=True, verbose_name='Родительская категория')
#     slug = models.SlugField()