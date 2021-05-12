from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name= 'login'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name= 'logout'),
    path('register/', RegisterPage.as_view(), name= 'register'),

    path('', views.paginator, name='task-list'),
    path('', TaskList.as_view(), name= 'tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name= 'task'),
    path('task-create/', TaskCreate.as_view(), name= 'task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name= 'task-update'),
    path('deletetask/<int:id>', views.deleteTask, name= 'delete-task'),

]