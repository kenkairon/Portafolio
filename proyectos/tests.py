from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date, timedelta
from .models import Proyecto

class ProyectoModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='testuser', password='12345')

    def test_crear_proyecto_valido(self):
        proyecto = Proyecto.objects.create(
            usuario=self.usuario,
            titulo='Proyecto Test',
            descripcion='Descripción del proyecto',
            fecha_inicio=date.today(),
            fecha_finalizacion=date.today() + timedelta(days=10),
            estado='pendiente'
        )
        self.assertEqual(str(proyecto), 'Proyecto Test')
        self.assertEqual(proyecto.estado, 'pendiente')

    def test_fecha_finalizacion_anterior_a_inicio_lanza_error(self):
        proyecto = Proyecto(
            usuario=self.usuario,
            titulo='Proyecto Inválido',
            descripcion='Fechas incorrectas',
            fecha_inicio=date.today(),
            fecha_finalizacion=date.today() - timedelta(days=1),
            estado='pendiente'
        )
        with self.assertRaises(ValidationError) as cm:
            proyecto.clean()  # Llama a clean() explícitamente
        self.assertIn('fecha de finalización no puede ser anterior', str(cm.exception))

    def test_estado_no_valido_lanza_error(self):
        proyecto = Proyecto(
            usuario=self.usuario,
            titulo='Estado inválido',
            descripcion='Prueba estado',
            fecha_inicio=date.today(),
            fecha_finalizacion=date.today() + timedelta(days=5),
            estado='cancelado'  # No es opción válida
        )
        with self.assertRaises(ValidationError):
            proyecto.full_clean()  # Esto validará choices y clean()

    def test_estado_valido(self):
        for estado_valido in ['pendiente', 'en_progreso', 'completado']:
            proyecto = Proyecto(
                usuario=self.usuario,
                titulo=f'Proyecto {estado_valido}',
                descripcion='Prueba estado válido',
                fecha_inicio=date.today(),
                fecha_finalizacion=date.today() + timedelta(days=5),
                estado=estado_valido
            )
            # No debe lanzar error
            proyecto.full_clean()
