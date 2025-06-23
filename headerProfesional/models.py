from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from iconos.models import Icono  # Asegúrate que esta app esté registrada en INSTALLED_APPS
from django.core.exceptions import ValidationError
# Opciones de nivel
NIVEL_CHOICES = [
    ('basico', 'Basico'),
    ('intermedio', 'Intermedio'),
    ('avanzado', 'Avanzado'),   
    ('experto', 'Experto'),
]
class Habilidad(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habilidades')
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50, choices=NIVEL_CHOICES, blank=True, default='')
    icono = models.ForeignKey(Icono, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def clean(self):
        if not self.usuario_id:
            return

        # Limpiar y capitalizar el nombre
        self.nombre = self.nombre.strip().capitalize()

        # Validar si ya existe una habilidad con ese nombre para el mismo usuario (insensible a mayúsculas)
        if Habilidad.objects.filter(
            usuario_id=self.usuario_id,
            nombre__iexact=self.nombre
        ).exclude(pk=self.pk).exists():
            raise ValidationError({'nombre': f'La habilidad "{self.nombre}" ya existe para este usuario.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # 👈 esto ejecuta clean() automáticamente
        super().save(*args, **kwargs)



class Header(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, default='Nombre')
    segundo_nombre = models.CharField(max_length=100, blank=True, default='')
    primer_apellido = models.CharField(max_length=100, default='Apellido')
    segundo_apellido = models.CharField(max_length=100, blank=True, default='')
    cargo_profesional = models.CharField(max_length=200, default='Desarrollador Web')
    imagen = models.ImageField(upload_to='headers/', blank=True, null=True)


    # Información de contacto
    email = models.EmailField(max_length=254, blank=True, default='')
    linkedin = models.URLField(max_length=200, blank=True, default='')
    github = models.URLField(max_length=200, blank=True, default='')
    telefono = models.CharField(
        max_length=20,
        blank=True,
        default='',
        validators=[RegexValidator(
            regex=r'^\+?\d{7,15}$',
            message="Ingrese un número de teléfono válido (mínimo 7 dígitos, con o sin +)."
        )]
    )

    def __str__(self):
        return f"{self.nombre} {self.primer_apellido}"