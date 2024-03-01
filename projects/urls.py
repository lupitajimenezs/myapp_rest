from rest_framework import routers
from .api import ProjectViewSet, TaskViewSet
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register("api/projects", ProjectViewSet, "projects")
router.register("api/tasks", TaskViewSet, "tasks")

urlpatterns = router.urls

urlpatterns += [
    path('index/', views.index),
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('tasks/<int:task_id>/delete', views.delete_task, name="delete_tasks"),
    path('tasks/<int:task_id>/complete', views.complete_task, name="complete_task"),
    path('tasks/<int:task_id>/cancelar', views.cancelar_task, name="cancelar_task"),
    path('tasks/<int:task_id>/', views.task_detail, name="task_detail"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project"),
]