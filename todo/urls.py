from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('todo/', todoView),
]
