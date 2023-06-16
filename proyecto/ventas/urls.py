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

    path('Clientes.html', views.clientes, name='Clientes'),
    path('lista_clientes',views.lista_clientes,name='lista_clientes'),
    path('Clientes_add',views.agregar_clientes,name='Clientes_add'),
    path('borrarCliente/<str:pk>',views.eliminar_clientes,name='cliente_del'),
    path('buscarCliente/<str:pk>',views.buscar_cliente,name='cliente_findEdit'),
    path('actualizarCliente',views.actualizar_cliente,name='actualizar_cliente'),

    path('listar_articulos', views.mostrar_articulos, name='crud_articulos'),
    path('agregar_articulos',views.agregar_articulos,name='articulosAdd'),
    path('borrar_articulos/<str:pk>',views.borrar_articulo,name='articulos_del'),
    path('actualizar_articulos/<str:pk>',views.actualizar_articulo,name='articulos_edit'),

     ]