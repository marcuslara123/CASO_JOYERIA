from django.urls import path
from . import views


urlpatterns = [
        path('index' ,views.inicio, name='index'),
         path('Anillos.html/', views.anillos, name='anillos'),
         path('RegistroJS.html/', views.registrojs, name='registrojs'),
        
        ]
