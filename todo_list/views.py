from django.shortcuts import render
from .models import Todo

# Create your views here.

def home(request, *args, **kwargs):
	return render(request, "home.html", {})

def todos_view(request, *args, **kwargs):
	context = {
		'site':'YouTube',
		'name':'Nem',
	}	
	return render(request,"todos.html",context)