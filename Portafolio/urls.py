"""
URL configuration for Portafolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings  # <-- asegúrate de tener esta línea
from django.conf.urls.static import static  # <-- y esta también
from django.conf.urls import handler404
from error_pages.views import error_404

urlpatterns = [
    path('', lambda request: redirect('home')), 
    path('admin/', admin.site.urls),
    path('accounts/', include('Accounts.urls')),  
    path('home/', include('home.urls')),
    path('header/', include('headerProfesional.urls')),
    path('objetivo/', include('objetivo.urls')), 
    path('proyectos/', include('proyectos.urls')),
    path('certificaciones/', include('certificaciones.urls')),
    path('iconos/', include('iconos.urls')),
    path('blog/', include('blog.urls')),
    path('contacto/', include('contacto.urls')),
]

# Solo se añade esto si estás en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Manejo de errores
handler404 = 'error_pages.views.error_404'
