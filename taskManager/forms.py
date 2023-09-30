from django import forms
from .models import Sprint, Task

class SprintForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = ['sprintName','sprintCreatedBy','sprintDataPoints','sprintDate']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['taskName','taskDescription','taskAssignee','taskPoints', 'taskState', 'sprintName']