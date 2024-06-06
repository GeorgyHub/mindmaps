from django import forms
from .models import Questions, Answers, CommentUser

# Create questions
class QuestionForm(forms.ModelForm):
	
	class Meta:
		model = Questions
		fields = ('name',)

	def __init__(self, *args, **kwargs):
		super(QuestionForm, self).__init__(*args, **kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'


class AnswersForm(forms.ModelForm):

	class Meta:
		model = Answers
		fields = ('title', 'text', 'question')

	def __init__(self, *args, **kwargs):
		super(AnswersForm, self).__init__(*args, **kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

# #
# class CommentsForm(forms.ModelForm):

# 	class Meta:
# 		model = CommentUser
# 		fields = ('text',)

# 	def __init__(self, *args, **kwargs):
# 		super(CommentsForm, self).__init__(*args, **kwargs)