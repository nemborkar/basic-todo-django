from django.shortcuts import render
# from todo_list import models

# Create your views here.

def home(request, *args, **kwargs):
    return render(request, "home.html", {})



def todos_view(request, *args, **kwargs):
    return render(request, "todos.html", {})