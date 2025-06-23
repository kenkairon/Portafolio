# iconos/models.py
from django.db import models
from django.contrib.auth.models import User
class Icono(models.Model):
    LIBRERIAS = [
        ('bootstrap', 'Bootstrap Icons'),
        ('fontawesome', 'Font Awesome'),
        ('otros', 'Otro'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    clase_css = models.CharField(max_length=100)
    libreria = models.CharField(max_length=50, choices=LIBRERIAS)
    def __str__(self):
        return f"{self.nombre}"
 
    class Meta:
        unique_together = ('usuario', 'clase_css') 