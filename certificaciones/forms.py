from django import forms
from .models import Certificacion

class CertificacionForm(forms.ModelForm):
    class Meta:
        model = Certificacion
        exclude = ['usuario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la certificación'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'enlace': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enlace a la certificación (opcional)'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_finalizacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
