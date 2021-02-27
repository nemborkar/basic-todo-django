from django import forms
from .models import Todo

class ListForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ["title","completed"]

	"""docstring for ClassName"""
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg
		