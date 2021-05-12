from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task

from rest_framework.permissions import IsAuthenticated


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class TaskList(LoginRequiredMixin, ListView):
    permission_classes = (IsAuthenticated, )

    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user= self.request.user)
        context['count'] = context['tasks'].filter(complete= False).count()
        
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains= search_input)
        context['search_input'] = search_input

        return context
        

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields =  ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


def deleteTask(request, id):
    task = get_object_or_404(Task, pk= id)
    task.delete()
    messages.info(request, "Task successfully deleted.")
    return redirect("/")


def paginator(request):
    tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)
    paginator = Paginator(tasks_list, 8)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)

    return render(request, "base/task_list.html", {'tasks' : tasks})