# Generated by Django 4.2.9 on 2024-05-19 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_alter_authors_deathday_alter_authors_deathlace'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=600, verbose_name='Запись')),
            ],
        ),
        migrations.RemoveField(
            model_name='authors',
            name='is_published',
        ),
        migrations.AddField(
            model_name='answers',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='authors.authors', verbose_name='Публицист'),
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='authors.questions', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.CharField(max_length=250, verbose_name='Ответ'),
        ),
    ]