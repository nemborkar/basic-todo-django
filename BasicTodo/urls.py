from django.contrib import admin
from django.urls import path, include
from todo_list.views import home, todos_view, toapp_view

# from myapi.views import HeroViewSet

urlpatterns = [
    path('', home, name="home"),
    path('todos/', todos_view, name="todos"),
    path('admin/', admin.site.urls),
    path('test/', toapp_view),
    path('my_api', include('myapi.urls')),
]
