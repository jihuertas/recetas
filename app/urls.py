from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    path('relaciones', views.relaciones, name='relaciones'),

    path('ingredientes', views.ingredientes_lista, name='ingredientes_lista'),
    path('ingredientes/nuevo', views.ingredientes_nuevo, name='ingredientes_nuevo'),
    path('ingredientes/nuevomodel', views.ingredientes_nuevo_model, name='ingredientes_nuevo_model'),
]