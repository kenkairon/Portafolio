from django import forms
from .models import ObjetivoProfesional
from iconos.models import Icono

class ObjetivoForm(forms.ModelForm):
    class Meta:
        model = ObjetivoProfesional
        fields = ['titulo', 'descripcion', 'icono', 'link', 'orden', 'modo_presentacion']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Título del objetivo'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Descripción'
            }),
            'icono': forms.Select(attrs={'class': 'form-select'}),
            'link': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'URL opcional'
            }),
            'orden': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Número de orden'
            }),
            'modo_presentacion': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Filtrar iconos solo del usuario actual
        if user:
            self.fields['icono'].queryset = Icono.objects.filter(usuario=user)
        else:
            self.fields['icono'].queryset = Icono.objects.none()

        # Determinar el valor actual de modo_presentacion
        modo = None
        if self.instance and self.instance.pk:
            modo = self.instance.modo_presentacion
        elif 'modo_presentacion' in self.data:
            modo = self.data.get('modo_presentacion')
        elif 'modo_presentacion' in self.initial:
            modo = self.initial.get('modo_presentacion')

        # Ajustar tamaño y estilo de descripción si modo es 'parrafo'
        if modo == 'parrafo':
            self.fields['descripcion'].widget.attrs['rows'] = 8
            self.fields['descripcion'].widget.attrs['style'] = 'font-size: 1.1rem; line-height: 1.5;'

        # Preparar líneas para el template si hay descripción
        if self.instance and self.instance.descripcion:
            self.descripcion_lineas = self.instance.descripcion.strip().split('\n')
        else:
            self.descripcion_lineas = []
