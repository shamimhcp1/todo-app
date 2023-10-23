from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('edit_todo/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('complete_todo/<int:todo_id>/', views.complete_todo, name='complete_todo')
]