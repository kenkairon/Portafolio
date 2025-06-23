from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_header, name='mostrar_header'),
    path('crear/', views.crear_header, name='crear_header'),
    path('editar/', views.editar_header, name='editar_header'),
    path('eliminar/', views.eliminar_header, name='eliminar_header'),
    path('habilidades/', views.lista_habilidades, name='lista_habilidades'),
    path('habilidades/crear/', views.crear_habilidad, name='crear_habilidad'),
    path('habilidades/editar/<int:pk>/', views.editar_habilidad, name='editar_habilidad'),
    path('habilidades/eliminar/<int:pk>/', views.eliminar_habilidad, name='eliminar_habilidad'),
]