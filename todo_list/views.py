from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import ListForm


# Create your views here.

def home(request):
	if request.method == "POST":
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = Todo.objects.all
			messages.success(request, ('Task has been added to the list'))
			return render(request, 'home.html', {'all_items': all_items})
		else:
			all_items = Todo.objects.all
			messages.success(request, ('This is showing from the inner else'))
			return render(request, 'home.html', {'all_items': all_items})	
	else:
		all_items = Todo.objects.all
		return render(request, 'home.html', {'all_items': all_items})


# def home(request, *args, **kwargs):
# 	return render(request, "home.html", {})

def todos_view(request, *args, **kwargs):
	todo_obj = Todo.objects.all()[:10]
	context = {
		'todo':todo_obj
	}	
	return render(request,"todos.html",context)

def toapp_view(request):
	response = redirect('/todos/')
	return response