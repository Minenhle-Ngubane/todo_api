from django.urls import path

from .views import (
    ListTodo, 
    DetailTodo, 
    CreateTodo, 
    UpdateTodo, 
    DeleteTodo
)

urlpatterns = [
    path('', ListTodo.as_view(), name='todo_list'),
    path('create/', CreateTodo.as_view(), name='todo_create'),
    path('<uuid:pk>/', DetailTodo.as_view(), name='todo_detail'),
    path('<uuid:pk>/update/', UpdateTodo.as_view(), name='todo_update'),
    path('<uuid:pk>/delete/', DeleteTodo.as_view(), name='todo_delete'),
]
