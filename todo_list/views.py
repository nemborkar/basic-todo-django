from django.shortcuts import render
from .models import Todo

# Create your views here.

def home(request, *args, **kwargs):
	return render(request, "home.html", {})

def todos_view(request, *args, **kwargs):
	todo_obj = Todo.objects.all()[:10]
	context = {
		'todo':todo_obj
	}	
	return render(request,"todos.html",context)