from django.test import TestCase
from django.contrib.auth.models import User
from .models import Habilidad, Header
from iconos.models import Icono


class HabilidadHeaderModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='testuser', password='12345')
        self.icono = Icono.objects.create(
            nombre='Python',
            clase_css='fab fa-python',
            usuario=self.usuario  # 👈 Agrega esta línea
        )


    def test_crear_habilidad(self):
        habilidad = Habilidad.objects.create(
            usuario=self.usuario,
            nombre='Python',
            nivel='avanzado',
            icono=self.icono
        )
        self.assertEqual(habilidad.nombre, 'Python')
        self.assertEqual(habilidad.usuario.username, 'testuser')
        self.assertEqual(habilidad.nivel, 'avanzado')
        self.assertEqual(str(habilidad), 'Python')

    def test_crear_header(self):
        Header.objects.create(
            usuario=self.usuario,
            nombre='Carlos',
            primer_apellido='Pérez',
            email='carlos@example.com',
            linkedin='https://linkedin.com/in/carlos',
            github='https://github.com/carlosdev',
            telefono='123456789'
        )

        header = Header.objects.get(usuario=self.usuario)
        self.assertEqual(str(header), 'Carlos Pérez')
        self.assertEqual(header.email, 'carlos@example.com')
        self.assertEqual(header.github, 'https://github.com/carlosdev')

    def test_usuario_no_puede_tener_dos_headers(self):
        Header.objects.create(usuario=self.usuario, nombre='Carlos', primer_apellido='Pérez')

        with self.assertRaises(Exception):  # OneToOneField lanzará IntegrityError
            Header.objects.create(usuario=self.usuario, nombre='Otro', primer_apellido='Apellido')
