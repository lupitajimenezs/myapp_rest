from django import forms
from .models import Task
from django.forms import ModelForm

class CreateNewTask(forms.Form):
    title = forms.CharField(
        label="Titulo de la tarea",
        max_length=200,
        widget=forms.TextInput(attrs={"class":"input"})
    )
    description = forms.CharField(
        label = "Descripcion de la tarea",
        widget=forms.Textarea(attrs={"class": "input"})
    )

class CreateNewProject(forms.Form):
    name = forms.CharField(
        label="Nombre del proyecto",
        max_length=200,
        widget=forms.TextInput(attrs={"class": "input"})
    )

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']