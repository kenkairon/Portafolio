import os
import django
import sys

# Configura el entorno Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portafolio.settings')
django.setup()

from django.contrib.auth.models import User
from iconos.models import Icono

# Mapeo de tipo de íconos
ICONO_TIPOS = {
    'facebook': 'fab',
    'twitter': 'fab',
    'linkedin': 'fab',
    'user': 'fas',
    'address-card': 'far',
    # Agrega más si es necesario
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_ICONOS = os.path.join(BASE_DIR, 'svg')

def cargar_iconos_desde_svg():
    print(f"🔍 Buscando SVGs en: {RUTA_ICONOS}")

    if not os.path.exists(RUTA_ICONOS):
        print(f"❌ Ruta no encontrada: {RUTA_ICONOS}")
        return

    try:
        admin = User.objects.get(username='admin')
    except User.DoesNotExist:
        print("⚠️ El usuario 'admin' no existe. Usa otro nombre o crea el superusuario con: python manage.py createsuperuser")
        return

    archivos_svg = [f for f in os.listdir(RUTA_ICONOS) if f.lower().endswith('.svg')]

    if not archivos_svg:
        print("⚠️ No se encontraron archivos .svg en la carpeta.")
        return

    cargados = 0
    for archivo in archivos_svg:
        nombre = archivo.replace('.svg', '').strip()
        tipo = ICONO_TIPOS.get(nombre, 'fas')  # por defecto 'fas'
        clase_css = f"{tipo} fa-{nombre}"

        if not Icono.objects.filter(clase_css=clase_css).exists():
            Icono.objects.create(
                usuario=admin,
                nombre=nombre,
                clase_css=clase_css,
                libreria='fontawesome'
            )
            cargados += 1
            print(f"✅ Importado: {nombre}")
        else:
            print(f"ℹ️ Ya existe: {nombre}")

    print(f"\n🎉 Proceso completado. Íconos nuevos importados: {cargados}")

if __name__ == '__main__':
    cargar_iconos_desde_svg()

