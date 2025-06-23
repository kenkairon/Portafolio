from django.contrib import admin
from .models import ObjetivoProfesional

@admin.register(ObjetivoProfesional)
class ObjetivoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'usuario')
    ordering = ('orden',)
