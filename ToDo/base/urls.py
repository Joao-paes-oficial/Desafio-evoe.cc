from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, CustomLoginView, RegisterPage
from . import views

urlpatterns = [
    path('', TaskList.as_view(), name= 'tasks'),
    path('task-create/', TaskCreate.as_view(), name= 'task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name= 'task-update'),
    path('deletetask/<int:id>', views.deleteTask, name= 'delete-task'),

]