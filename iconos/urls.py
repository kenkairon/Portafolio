from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_iconos, name='listar_iconos'),
    path('crear/', views.crear_icono, name='crear_icono'),
    path('editar/<int:pk>/', views.editar_icono, name='editar_icono'),
    path('eliminar/<int:pk>/', views.eliminar_icono, name='eliminar_icono'),
]
