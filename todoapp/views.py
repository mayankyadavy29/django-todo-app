from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

class TaskListView(ListView):
    model = Task
    template_name = 'todoapp/index.html'
    context_object_name = 'task_list'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'todoapp/detail.html'
    context_object_name = 'task'

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'todoapp/edit.html'
    context_object_name = 'task'
    fields = ['name', 'priority', 'date']

    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail', kwargs={'pk': self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todoapp/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('todoapp:cbvindex')

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date', '')
        new_task = Task(name=name, priority=priority, date=date)
        new_task.save()
        return redirect('/')
    task_list = Task.objects.all()
    return render(request, 'todoapp/index.html', {'task_list': task_list})

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'todoapp/delete.html', {'task': task})

def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    print(task.date)
    if request.method == 'POST':
        print("Yesesesesesesee")
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        Task.objects.filter(id=task_id).update(name=name, priority=priority, date=date)
        return redirect('/')
    return render(request, 'todoapp/edit.html', {'task': task})