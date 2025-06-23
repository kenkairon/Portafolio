from django.test import TestCase
from django.contrib.auth.models import User
from .models import Icono
from django.db import IntegrityError
from django.core.exceptions import ValidationError

class IconoModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='123')
        self.user2 = User.objects.create_user(username='user2', password='123')

    def test_crear_icono_valido(self):
        icono = Icono.objects.create(
            usuario=self.user1,
            nombre='Python',
            clase_css='fab fa-python',
            libreria='fontawesome'
        )
        self.assertEqual(str(icono), 'Python')
        self.assertEqual(icono.libreria, 'fontawesome')

    def test_no_se_permite_icono_duplicado_para_mismo_usuario_y_clase_css(self):
        Icono.objects.create(
            usuario=self.user1,
            nombre='Python',
            clase_css='fab fa-python',
            libreria='fontawesome'
        )

        with self.assertRaises(IntegrityError):
            Icono.objects.create(
                usuario=self.user1,
                nombre='Otro nombre',
                clase_css='fab fa-python',  # misma clase
                libreria='fontawesome'
            )

    def test_se_permite_mismo_clase_css_para_diferente_usuario(self):
        Icono.objects.create(
            usuario=self.user1,
            nombre='Python',
            clase_css='fab fa-python',
            libreria='fontawesome'
        )
        try:
            Icono.objects.create(
                usuario=self.user2,
                nombre='Python icon',
                clase_css='fab fa-python',
                libreria='fontawesome'
            )
        except IntegrityError:
            self.fail("No debería lanzar error porque es otro usuario")

    def test_libreria_invalida_lanza_error(self):
        icono = Icono(
            usuario=self.user1,
            nombre='Java',
            clase_css='fab fa-java',
            libreria='invalida'
        )
        with self.assertRaises(ValidationError):
            icono.full_clean()  # valida el campo 'choices'
