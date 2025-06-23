# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.certificacion_list, name='certificacion_list'),
    path('crear/', views.certificacion_create, name='certificacion_create'),
    path('editar/<int:pk>/', views.certificacion_update, name='certificacion_update'),
    path('eliminar/<int:pk>/', views.certificacion_delete, name='certificacion_delete'),
    path('certificaciones/pdf/', views.generar_pdf, name='generar_pdf'),
]
