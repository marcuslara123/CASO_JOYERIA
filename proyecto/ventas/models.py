from django.db import models

# Create your models here.


class Region(models.Model):
    id_region        = models.AutoField(db_column='idRegion', primary_key=True) 
    region           = models.CharField(max_length=20)

    def __str__(self):
        return str(self.region )
    

class Cliente(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=False, null=False) 
    id_region        = models.ForeignKey('Region', on_delete=models.CASCADE, db_column='idRegion') 
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   
    

    

