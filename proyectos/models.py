from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Proyecto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completado', 'Completado')
    ])

    def __str__(self):
        return self.titulo
    
    def clean(self):
        if self.fecha_finalizacion and self.fecha_inicio:
            if self.fecha_finalizacion < self.fecha_inicio:
                raise ValidationError('La fecha de finalización no puede ser anterior a la fecha de inicio.')

