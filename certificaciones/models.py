from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Certificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='certificaciones/')
    enlace = models.URLField(blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_finalizacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        if self.fecha_inicio and self.fecha_finalizacion:
            if self.fecha_finalizacion < self.fecha_inicio:
                raise ValidationError("La fecha de finalización no puede ser anterior a la fecha de inicio.")