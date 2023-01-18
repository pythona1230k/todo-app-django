from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from todo.models import Task



class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    # 全てのフィールドを使う
    fields = '__all__'
    # 新規タスクを作った後に飛ぶページの指定
    success_url = reverse_lazy('task-list')
    template_name = 'todo/task_form.html'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')
    template_name = 'todo/task_delete.html'


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    # 全てのフィールドを使う
    fields = '__all__'
    # 新規タスクを作った後に飛ぶページの指定
    success_url = reverse_lazy('task-list')
    template_name = 'todo/task_form.html'
