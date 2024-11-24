from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.list_todos, name='list_todos'),
    path('todos/add', views.add_todo),
    path('todo/update/<int:pk>/', views.update_todo),
    path('todo/delete/<int:pk>/', views.delete_todo),
]
