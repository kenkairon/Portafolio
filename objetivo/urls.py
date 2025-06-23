from django.urls import path
from . import views

urlpatterns = [
    path('', views.objetivo_list, name='objetivo_list'),
    path('crear/', views.objetivo_create, name='objetivo_create'),
    path('editar/<int:pk>/', views.objetivo_update, name='objetivo_update'),
    path('eliminar/<int:pk>/', views.objetivo_delete, name='objetivo_delete'),
]