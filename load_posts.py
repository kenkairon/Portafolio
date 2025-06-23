import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portafolio.settings')  # Cambia 'Portafolio' por el nombre de tu proyecto
django.setup()

from blog.models import Post  # Importar el modelo Post
from django.contrib.auth.models import User

def poblar_posts():
    # Obtener un usuario existente (puedes usar el primer usuario o crear uno si no existe)
    user = User.objects.first()
    if not user:
        print("No hay usuarios registrados. Por favor, crea al menos un usuario antes de ejecutar este script.")
        return

    # Datos de prueba para los posts
    posts = [
        {
            "title": "Primer Post",
            "content": "Este es el contenido del primer post.",
            "author": user.username,  # Usar el nombre de usuario como autor
        },
        {
            "title": "Segundo Post",
            "content": "Este es el contenido del segundo post.",
            "author": user.username,
        },
        {
            "title": "Tercer Post",
            "content": "Este es el contenido del tercer post.",
            "author": user.username,
        },
    ]

    # Poblar la base de datos con los posts
    for post_data in posts:
        Post.objects.create(**post_data)

    print("Posts de prueba creados exitosamente.")

if __name__ == '__main__':
    poblar_posts()