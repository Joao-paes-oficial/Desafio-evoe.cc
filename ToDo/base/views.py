from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task




class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'