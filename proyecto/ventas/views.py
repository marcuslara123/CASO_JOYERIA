
from django.shortcuts import render

from .models import Cliente, Articulo

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
    
    ## BASE DE DATOS 

def clientes(request):
     lista_clientes = Cliente.objects.all() #select * from Cliente
     context={"clientes":lista_clientes}
     return render(request,'ventas/Clientes.html',context)

def lista_clientes(request):
     lista_clientes = Cliente.objects.raw("SELECT * FROM ventas_clientes") #select * from Cliente
     context={"clientes":lista_clientes}
     return render(request,'ventas/Clientes.html',context)

def agregar_clientes(request):
    if request.method != "POST":
        lista_articulos = Articulo.objects.all()
        context={"articulos":lista_articulos}
        return render(request,'ventas/Clientes_add.html',context)
    else:
         #rescatamos en variables os valores del formulario (name)
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        ape_Pat = request.POST["apePat"]
        ape_Mat = request.POST["apeMat"]
        fec_Nac = request.POST["fecNac"]
        N_articulo = request.POST["N_articulo"] #NOMBRE ARTICULO
        email = request.POST["email"]
        direccion = request.POST["dire"]

        objArticulo = Articulo.objects.get(articulo = N_articulo)
        
        #crea alumno (izp:nombre del campo de la BD, derecho:variable local)
        objCliente = Cliente.objects.create(  
            rut              = rut,
            nombre           = nombre,
            apellido_paterno = ape_Pat,
            apellido_materno = ape_Mat,
            fecha_nacimiento = fec_Nac,
            articulo       = objArticulo, 
            email            = email,
            direccion        = direccion,
            activo           = 1)
        
        objCliente.save() #insert en la base de datos
        lista_articulos = Cliente.objects.all()
        context = {"mensaje":"Se guardó cliente","articulos":lista_articulos}
        return render(request,'ventas/Clientes_add.html',context)
        
def eliminar_clientes(request,pk):
    
    try:
        cliente = Cliente.objects.get(rut=pk)

        cliente.delete() #delete en la BD
        mensaje = "Se eliminó Cliente"
        lista_clientes = Cliente.objects.all()
        context={"cliente":lista_clientes, "mensaje":mensaje}
        return render(request,'ventas/clientes.html',context)
    except:
        mensaje = "NO se eliminó cliente"
        lista_clientes = Cliente.objects.all()
        context={"cliente":lista_clientes, "mensaje":mensaje}
        return render(request,'ventas/Clientes.html',context)
    
def buscar_cliente(request,pk):
     if pk != "":
        cliente = Cliente.objects.get(rut=pk)
        lista_articulos = Cliente.objects.all()
        context={"cliente":cliente, "Clientes":lista_articulos}
        if cliente:
            return render(request,'ventas/clientes_edit.html',context)
        else:
            context = {"mensaje":"El cliente no existe"}
            return render(request,'ventas/Clientes.html',context)
        
def actualizar_cliente(request):
     if request.method == "POST":
         #rescatamos en variables los valores del formulario (name)
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        ape_Pat = request.POST["apePat"]
        ape_Mat = request.POST["apeMat"]
        fec_Nac = request.POST["fecNac"]
        N_articulo = request.POST["N_articulo"]   
        email = request.POST["email"]
        direccion = request.POST["dire"]
       

        objArticulo = Articulo.objects.get(articulo = N_articulo)
        
         #crea alumno (izp:nombre del campo de la BD, derecho:variable local)
        objCliente = Cliente()
        objCliente.rut              = rut
        objCliente.nombre           = nombre
        objCliente.apellido_paterno = ape_Pat
        objCliente.apellido_materno = ape_Mat
        objCliente.fecha_nacimiento = fec_Nac
        objCliente.articulo        = objArticulo
        objCliente.email            = email
        objCliente.direccion        = direccion
        objCliente.activo           = 1
        
        objCliente.save() #update en la base de datos
        lista_articulos = Cliente.objects.all()
        context = {"mensaje":"Se guardó cliente","articulos":lista_articulos}
        return render(request,'ventas/Clientes_add.html',context)
     else:
        lista_clientes = Cliente.objects.all()
        context = {"clientes":lista_clientes}
        return render(request,'ventas/Clientes.html',context) 