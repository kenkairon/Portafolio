from django import forms
from .models import Certificacion

class CertificacionForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'},
            format='%Y-%m-%d'  
        )
    )
    fecha_finalizacion = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'},
            format='%Y-%m-%d'
        )
    )

    class Meta:
        model = Certificacion
        exclude = ['usuario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'enlace': forms.URLInput(attrs={'class': 'form-control'}),
        }
