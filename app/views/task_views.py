from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import TaskForm
from app.models import Task
from app.services import task_service


def home(request):
    return redirect(request, 'index_tasks')


@login_required()
def index_tasks(request):
    tasks = task_service.index_tasks(request.user)
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


@login_required()
def create_task(request):
    page_title = "Criar Tarefa"
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            title = task_form.cleaned_data["title"]
            description = task_form.cleaned_data["description"]
            expiration_date = task_form.cleaned_data["expiration_date"]
            priority = task_form.cleaned_data["priority"]
            new_task = Task(title=title, description=description,
                            expiration_date=expiration_date,
                            priority=priority, user=request.user)
            task_service.create_task(new_task)
            return redirect('index_tasks')
    else:
        task_form = TaskForm()
    return render(request, 'tasks/task_form.html', {
        'task_form': task_form, 'page_title': page_title})


@login_required()
def update_task(request, id):
    page_title = "Editar Tarefa"
    task = task_service.search_task_id(id)
    if task.user != request.user:
        return HttpResponse(
            "Opa!! parece que você está tentando alterar uma tarefa que não é sua")
    task_form = TaskForm(request.POST or None, instance=task)

    if task_form.is_valid():
        title = task_form.cleaned_data["title"]
        description = task_form.cleaned_data["description"]
        expiration_date = task_form.cleaned_data["expiration_date"]
        priority = task_form.cleaned_data["priority"]
        updated_task = Task(title=title, description=description,
                            expiration_date=expiration_date, priority=priority,
                            user=request.user)

        task_service.update_task(task, updated_task)
        return redirect('index_tasks')
    return render(request, 'tasks/task_form.html', {
        'task_form': task_form, 'page_title': page_title})


@login_required()
def delete_task(request, id):
    task = task_service.search_task_id(id)
    if task.user != request.user:
        return HttpResponse(
            "Opa!! parece que você está tentando apagar uma tarefa que não é sua")
    if request.method == "POST":
        task_service.delete_task(task)
        return redirect('index_tasks')
    return render(request, 'tasks/delete_confirmation.html', {'task': task})
