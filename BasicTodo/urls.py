
from django.contrib import admin
from django.urls import path
from todo_list.views import todos_view, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('todos/', todos_view),
]
