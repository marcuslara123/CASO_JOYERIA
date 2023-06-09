from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Index.html', views.inicio, name='inicio'),
    path('Anillos.html', views.anillo, name='anillo'),
    path('Collares.html', views.collar, name='collar'),
    path('Pendientes.html', views.pendiente, name='pendiente'),
    path('Brazaletes.html', views.brazalete, name='brazalete'),
    path('Registro.html', views.registro, name='registro'),
    path('Carro.html', views.carro, name='carro'),
    path('RegistroJS.html', views.registrojs, name='registrojs'),
    path('IniciarSesion.html', views.iniciarsesion, name='iniciarsesion'),
    path('clientes_add', views.agregar_clientes, name='clientes_add'),
]