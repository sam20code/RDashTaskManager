from django import forms
from .models import Sprint

class SprintForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = ['sprintName','sprintCreatedBy','sprintDataPoints','sprintDate']