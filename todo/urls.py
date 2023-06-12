from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('completed/<int:pk>/', views.taskCompleted, name='completed'),
    path('notcompleted/<int:pk>/', views.tasknotCompleted, name='notcompleted'),
    path('edit/<int:pk>/', views.taskedit, name='edit'),
    path('delete/<int:pk>/', views.taskdelete, name='delete')
]
