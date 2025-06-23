from django.test import TestCase
from django.contrib.auth.models import User
from .models import Certificacion
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError

class CertificacionModelTest(TestCase):
    
    # Test Agregar validación en el modelo 
    def setUp(self):
        self.usuario = User.objects.create_user(username='testuser', password='12345')
        self.imagen = SimpleUploadedFile(
            name='test_cert.jpg',
            content=b'file_content',
            content_type='image/jpeg'
        )
        
    # Test: Crear una certificación con fecha de inicio y finalización válidas
    def test_fecha_finalizacion_antes_de_inicio(self):
        cert = Certificacion(
            usuario=self.usuario,
            nombre='Cert inválido',
            imagen=self.imagen,
            fecha_inicio=date(2024, 5, 1),
            fecha_finalizacion=date(2024, 4, 1)
        )
        with self.assertRaises(ValidationError) as context:
            cert.full_clean()  # Ejecuta las validaciones del modelo

        self.assertIn('La fecha de finalización no puede ser anterior a la fecha de inicio.', str(context.exception))