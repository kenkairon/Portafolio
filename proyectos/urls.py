from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_proyectos, name='lista_proyectos'),
    path('proyecto/<int:pk>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('proyecto/nuevo/', views.nuevo_proyecto, name='nuevo_proyecto'),
    path('proyecto/<int:pk>/editar/', views.editar_proyecto, name='editar_proyecto'),
    path('proyecto/<int:pk>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),
]