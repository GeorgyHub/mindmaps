from django.contrib import admin
from .models import Authors, Questions, Answers, Post

# Register your models here.
admin.site.register(Authors)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Post)