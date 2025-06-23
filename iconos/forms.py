from django import forms
from .models import Icono

class IconoForm(forms.ModelForm):
    class Meta:
        model = Icono
        fields = ['nombre', 'clase_css', 'libreria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del icono'}),
            'clase_css': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Clase del icono (ej. fa fa-home)'}),
            'libreria': forms.Select(attrs={'class': 'form-select'}),
        }


