
from django.shortcuts import render

from .models import Cliente

# Create your views here.
def inicio(request):
    context = {}
    return render(request, 'ventas/index.html', context)

def anillo(request):
    context = {}
    return render(request, 'ventas/anillos.html', context)

def collar(request):
    context = {}
    return render(request, 'ventas/collares.html', context)

def pendiente(request):
    context = {}
    return render(request, 'ventas/pendientes.html', context)

def brazalete(request):
    context = {}
    return render(request, 'ventas/brazaletes.html', context)

def registro(request):
    context = {}
    return render(request, 'ventas/registro.html', context)

def carro(request):
    context = {}
    return render(request, 'ventas/carro.html', context)

def registrojq(request):
    context = {}
    return render(request, 'ventas/registrojquery.html', context)

def registrojs(request):
    context = {}
    return render(request, 'ventas/registrojs.html', context)

def iniciarsesion(request):
    context = {}
    return render(request, 'ventas/iniciarsesion.html', context)

def agregar_clientes(request):
# EN EL METODO ES POST Y EN EL GENERO PODRIAN SER LOS ARTICULOS YA QUE ES UN COMBOBOX QUE SE 
#RECORRE QUE SE OBTIEENE DEL MODELS GENERO
    if request.method != 'POST':
       # generos=Genero.objects.all()
        #context={'generos':generos }
        context = {}
        return render(request,'venta/Clientes.html', context)
    else:
        id = request.POST["id"]
        nombre = request.POST["nombre"]
        apellido_paterno = request.POST["apePater"]
        apellido_materno = request.POST["ApeMater"]
        fecha_nacimiento = request.POST["fecNaci"]
        email = request.POST["email"]
    
        #objGenero = Genero.objects.get (id_genero = genero)
        objCliente= Cliente.objects.create (
            id              = id,
            nombre           = nombre,
            apellido_paterno = apePater,
            apellido_materno = apeMater,
            fecha_nacimiento = fecNaci,
           
            email            = email,
          
            activo           = 1)


# LUEGO SE GUARDA EN LA BASE DE DATOS CON EL MENSAJE ASOCIADO EN EL HTML

        objCliente.save()
        context = {"mensaje":"se guardaron los datos"}
        return render(request,'venta/alumnos_add.html',context)

                                            

