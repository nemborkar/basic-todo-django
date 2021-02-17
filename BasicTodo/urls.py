
from django.contrib import admin
from django.urls import path
from todo_list.views import todos_view, home

urlpatterns = [
    path('', home, name="home"),
    path('todos/', todos_view, name="todos"),
    path('admin/', admin.site.urls),
]
