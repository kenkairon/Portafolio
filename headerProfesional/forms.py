from django import forms
from .models import Header
from .models import Habilidad
from iconos.models import Icono

class HeaderForm(forms.ModelForm):
    class Meta:
        model = Header
        exclude = ['usuario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo Nombre'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Paterno'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Materno'}),
            'cargo_profesional': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profesión o Cargo'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Perfil de LinkedIn'}),
            'github': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Perfil de GitHub'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de teléfono'}),
           
        }

class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        exclude = ['usuario']
        fields = ['nombre', 'nivel', 'icono']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control col-6',
                'placeholder': 'Ej:Ingrese una habilidad que lo destaque',
                'maxlength': '50',
                'aria-label': 'Nombre de la habilidad'
            }),
            'nivel': forms.Select(attrs={
                'class': 'form-select',
                'aria-label': 'Selecciona el nivel de habilidad'
            }),
            'icono': forms.Select(attrs={
                'class': 'form-select',
                'aria-label': 'Selecciona un ícono representativo'
            }),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre.capitalize()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # obtener usuario que se pasa desde la vista
        super().__init__(*args, **kwargs)

        if user:
            self.fields['icono'].queryset = Icono.objects.filter(usuario=user)