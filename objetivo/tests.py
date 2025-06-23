from django.test import TestCase
from django.contrib.auth.models import User
from iconos.models import Icono
from .models import ObjetivoProfesional
from django.core.exceptions import ValidationError

class ObjetivoProfesionalModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.icono = Icono.objects.create(
            usuario=self.user,
            nombre='Objetivo Icon',
            clase_css='fas fa-bullseye',
            libreria='fontawesome'
        )

    def test_crear_objetivo_valido(self):
        objetivo = ObjetivoProfesional.objects.create(
            usuario=self.user,
            titulo='Mi objetivo',
            descripcion='Aprender Django a fondo.',
            icono=self.icono,
            link='https://example.com',
            modo_presentacion='parrafo'
        )
        self.assertEqual(str(objetivo), 'Mi objetivo')
        self.assertEqual(objetivo.orden, 1)  # Primer objetivo → orden 1

    def test_orden_automatico_incrementa(self):
        ObjetivoProfesional.objects.create(
            usuario=self.user,
            titulo='Primero',
            descripcion='Desc 1',
            modo_presentacion='parrafo'
        )
        segundo = ObjetivoProfesional.objects.create(
            usuario=self.user,
            titulo='Segundo',
            descripcion='Desc 2',
            modo_presentacion='parrafo'
        )
        self.assertEqual(segundo.orden, 2)

    def test_orden_personalizado_no_cambia(self):
        objetivo = ObjetivoProfesional.objects.create(
            usuario=self.user,
            titulo='Orden manual',
            descripcion='...',
            orden=7,
            modo_presentacion='parrafo'
        )
        self.assertEqual(objetivo.orden, 7)

    def test_modo_presentacion_invalido_lanza_error(self):
        objetivo = ObjetivoProfesional(
            usuario=self.user,
            titulo='Modo inválido',
            descripcion='...',
            modo_presentacion='tabla'  # ❌ No válido
        )
        with self.assertRaises(ValidationError):
            objetivo.full_clean()  # Valida las opciones del campo

    def test_icono_puede_ser_null(self):
        objetivo = ObjetivoProfesional.objects.create(
            usuario=self.user,
            titulo='Sin icono',
            descripcion='...',
            modo_presentacion='lista'
        )
        self.assertIsNone(objetivo.icono)

    def test_ordering_por_defecto(self):
        ObjetivoProfesional.objects.create(
            usuario=self.user,
            titulo='B',
            descripcion='...',
            orden=2,
            modo_presentacion='parrafo'
        )
        ObjetivoProfesional.objects.create(
            usuario=self.user,
            titulo='A',
            descripcion='...',
            orden=1,
            modo_presentacion='parrafo'
        )
        titulos = list(ObjetivoProfesional.objects.values_list('titulo', flat=True))
        self.assertEqual(titulos, ['A', 'B'])  # Ordenado por orden

