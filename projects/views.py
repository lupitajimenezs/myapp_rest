from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject, TaskForm

def hello(request, username):
    return HttpResponse("<h1>HOLA %s</h1>" % username)

def index(request):
    title = "Curso de Django"
    return render(
        request,
        'index.html',
        {
            "title": title
        }
    )

def projects(request):
    projects = Project.objects.all()
    return render(
        request,
        'projects/projects.html',
        {
            'projects': projects
        }
    )

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

def create_task(request):
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {"form": CreateNewTask()})
    else:
        Task.objects.create(
            title = request.POST["title"],
            description = request.POST["description"],
            project_id = 2
        )
        return redirect("tasks")
     
def create_project(request):
    if request.method == "GET":
        return render(request, "projects/create_project.html", {"form": CreateNewProject()})
    else:
        Project.objects.create(
            name = request.POST["name"]
        )
        return redirect("create_project")
    
def project_detail(request, id):
    project = get_object_or_404(Project, id = id)
    tasks = Task.objects.filter(project_id = id)
    return render(
        request,
        "projects/detail.html",
        {
            "projects" : project,
            "tasks": tasks
        }
    )


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'tasks/task_detail.html', {'task': task, 'form': form})
    else:
        try:
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'tasks/tasks.html', {'task': task, 'form': form, 'error': 'Error updating task.'})
        
def complete_task(
        request,
        task_id
    ):
    estado =True
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        task.done = estado
        task.save()
        return redirect('tasks')
    
def cancelar_task(
        request,
        task_id
    ):
    estado =False
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        task.done = estado
        task.save()
        return redirect('tasks')
    

def delete_task(request, task_id):
    task = get_object_or_404(
        Task,
        pk = task_id
    )
    if request.method == "POST":
        task.delete()
        return redirect("tasks")