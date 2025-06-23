from django import forms
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_finalizacion', 'estado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título del proyecto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descripción del proyecto'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_finalizacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
