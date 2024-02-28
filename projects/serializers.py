from rest_framework import serializers
from .models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        #definimos las filas.
        fields = (
            "id",
            "name"
        )
        read_only_fields = ("id",)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "description",
            "project",
            "done"
        )
        #definimos los campos que seran de solo lectura.
        read_only_fields = ("id",)