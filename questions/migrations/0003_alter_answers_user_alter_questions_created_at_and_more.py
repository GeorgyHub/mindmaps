# Generated by Django 4.2.9 on 2024-05-27 14:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0002_alter_answers_comment_alter_answers_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Вопрос пользователя'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 27, 17, 2, 30, 656060), verbose_name='Дата создание вопроса'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='user_quest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Вопрос пользователя'),
        ),
        migrations.AlterField(
            model_name='ratinganswer',
            name='answer',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, to='questions.answers', verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='ratinganswer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Вопрос пользователя'),
        ),
        migrations.AlterField(
            model_name='ratingcomment',
            name='comment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='questions.commentuser', verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='ratingcomment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Вопрос пользователя'),
        ),
    ]