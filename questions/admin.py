from django.contrib import admin
from .models import Questions, Answers, CommentUser, RatingAnswer, RatingComment

admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(CommentUser)
admin.site.register(RatingAnswer)
admin.site.register(RatingComment)