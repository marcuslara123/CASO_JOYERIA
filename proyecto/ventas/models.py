from django.db import models

# Create your models here.


class Cliente(models.Model):
    id            = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   
    
class Articulo(models.Model):
    idA             = models.CharField(primary_key=True, max_length=2)
    nombreArticulo         = models.CharField(max_length=20)
    precio  = models.IntegerField()
    stock = models.IntegerField()
    fecha_producto = models.DateField(blank=False, null=False) 
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombreArticulo)+" "+str(self.precio)   
    

    

