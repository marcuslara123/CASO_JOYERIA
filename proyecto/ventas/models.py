from django.db import models

# Create your models here.


class Articulo(models.Model):
    idA            = models.AutoField(db_column='idArticulo', primary_key=True) 
    articulo       = models.CharField(max_length=20)
    precio         = models.IntegerField()
    stock          = models.IntegerField()
    fecha_producto = models.DateField(blank=False, null=False) 

    def __str__(self):
        return str(self.articulo)+" "+str(self.precio)   
    

class Cliente(models.Model):
    id               = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    idA              = models.ForeignKey('Articulo',on_delete=models.CASCADE, db_column='idArticulo') 
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   
    

    

