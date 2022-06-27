from django.urls import path
from . import views

urlpatterns = [
    # Cuando el usuario acceda a la raiz, va a entrar a inicio y se mostrara
    path('inicio', views.inicio, name='inicio'),
    path('habitaciones', views.habitaciones, name='habitaciones'),
]
