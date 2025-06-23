from django.db import models 
from django.contrib.auth.models import User
from iconos.models import Icono  # Asegúrate de que este import esté correcto

class ObjetivoProfesional(models.Model):
    MODO_PRESENTACION = [
        ('parrafo', 'Párrafos'),
        ('lista', 'Lista desordenada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    icono = models.ForeignKey(Icono, on_delete=models.SET_NULL, null=True, blank=True)
    link = models.URLField(max_length=300, blank=True, null=True)
    orden = models.PositiveIntegerField(default=0, help_text="Usa números pequeños para ordenar manualmente")

    # ✅ Campo nuevo correctamente definido
    modo_presentacion = models.CharField(
        max_length=10,
        choices=MODO_PRESENTACION,
        default='parrafo'
    )
    def save(self, *args, **kwargs):
        if self.orden == 0:  # Solo si no lo han definido
            ultimo_orden = ObjetivoProfesional.objects.filter(usuario=self.usuario).aggregate(
                max_orden=models.Max('orden')
            )['max_orden'] or 0
            self.orden = ultimo_orden + 1
        super().save(*args, **kwargs)
    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['orden']

