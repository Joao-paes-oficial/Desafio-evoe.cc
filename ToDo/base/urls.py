from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, CustomLoginView, RegisterPage

urlpatterns = [
    path('', TaskList.as_view(), name= 'tasks'),

]