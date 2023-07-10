
from django.shortcuts import render
from .models import Cliente, Region
from .forms import RegionForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    request.session["usuario"]="UsuarioX"
    usuario=request.session["usuario"]
    context = {"usu":usuario}
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


@login_required
def clientes(request):
     request.session["usuario"]="UsuarioX"
     lista_clientes = Cliente.objects.all() #select * from Cliente
     usuario=request.session["usuario"]
     context={"clientes":lista_clientes,"usu":usuario}
     return render(request,'ventas/Clientes.html',context)

def lista_clientes(request):
    search_query = request.GET.get('search', '')
    clientes = Cliente.objects.filter(nombre__icontains=search_query)
    context = {"clientes": clientes}
    return render(request, 'ventas/Clientes.html', context)


@login_required
def agregar_clientes(request):
    if request.method != "POST":
        lista_region = Region.objects.all()
        context={"regions":lista_region}
        return render(request,'ventas/Clientes_add.html',context)
    else:
         #rescatamos en variables os valores del formulario (name)
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        ape_Pat = request.POST["apePat"]
        ape_Mat = request.POST["apeMat"]
        fec_Nac = request.POST["fecNac"]
        region = request.POST["region"] #NOMBRE ARTICULO
        email = request.POST["email"]
        direccion = request.POST["dire"]

        objRegion = Region.objects.get(id_region = region)
        
        #crea alumno (izp:nombre del campo de la BD, derecho:variable local)
        objCliente = Cliente.objects.create(  
            rut              = rut,
            nombre           = nombre,
            apellido_paterno = ape_Pat,
            apellido_materno = ape_Mat,
            fecha_nacimiento = fec_Nac,
            id_region       = objRegion, 
            email            = email,
            direccion        = direccion,
            activo           = 1)
        
        objCliente.save() #insert en la base de datos
        lista_region = Region.objects.all()
        context = {"mensaje":"Se guardó cliente!","regions":lista_region}
        return render(request,'ventas/Clientes_add.html',context)
        
def eliminar_clientes(request,pk):
    
    try:
        cliente = Cliente.objects.get(rut=pk)

        cliente.delete() #delete en la BD
        mensaje = "Se eliminó Cliente!"
        lista_clientes = Cliente.objects.all()
        context={"cliente":lista_clientes, "mensaje":mensaje}
        return render(request,'ventas/clientes.html',context)
    except:
        mensaje = "NO se eliminó cliente!"
        lista_clientes = Cliente.objects.all()
        context={"cliente":lista_clientes, "mensaje":mensaje}
        return render(request,'ventas/Clientes.html',context)
    
def buscar_cliente(request,pk):
     if pk != "":
        cliente = Cliente.objects.get(rut=pk)
        lista_region = Region.objects.all()
        context={"cliente":cliente, "regions":lista_region}
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
        region = request.POST["region"]   
        email = request.POST["email"]
        direccion = request.POST["dire"]
       

        objRegion = Region.objects.get(id_region = region)
        
         #crea alumno (izp:nombre del campo de la BD, derecho:variable local)
        objCliente = Cliente()
        objCliente.rut              = rut
        objCliente.nombre           = nombre
        objCliente.apellido_paterno = ape_Pat
        objCliente.apellido_materno = ape_Mat
        objCliente.fecha_nacimiento = fec_Nac
        objCliente.id_region        = objRegion
        objCliente.email            = email
        objCliente.direccion        = direccion
        objCliente.activo           = 1
        
        objCliente.save() #update en la base de datos
        lista_region = Region.objects.all()
        context = {"mensaje": "Cliente actualizado!", "cliente": objCliente, "regions": lista_region}

        return render(request,'ventas/Clientes_edit.html',context)
     else:
        lista_clientes = Cliente.objects.all()
        form = RegionForm()
        context = {"clientes":lista_clientes,"form": form}
        return render(request,'ventas/Clientes.html',context) 
     


     

def mostrar_articulos(request):
    lista_region = Region.objects.all()
    usuario=request.session["usuario"]
    context={"regions":lista_region,"usu":usuario}
    return render(request,'ventas/Articulos_list.html',context)

def agregar_articulos(request):
    if request.method == "POST":
        form = RegionForm(request.POST)
        if form.is_valid:
            form.save() #insert
            form = RegionForm()
            context = {"mensaje": "Se agregó artículo", "form":form}
            return render(request,'ventas/Articulos_add.html',context)
        
    else:
        form = RegionForm()
        context = {"form":form}
        return render(request,'ventas/Articulos_add.html',context)

def borrar_articulo(request,pk):
    errores = []
    try:
        articulo = Region.objects.get(id_region=pk)
        if articulo:
            articulo.delete()
            lista_region = Region.objects.all()
            context = {"mensaje": "Artículo eliminado", "regions":lista_region, "errores": errores}
            return render(request,'ventas/Articulos_list.html',context)
    
    except:
        lista_region = Region.objects.all() 
        context = {"mensaje": "No existe artículo", "regions":lista_region, "errores": errores}
        return render(request,'ventas/Articulos_list.html',context)
    
def actualizar_articulo(request, pk):
    try:
        region = Region.objects.get(id_region=pk)
        if region:
            if request.method == "POST":
                form = RegionForm(request.POST, instance=region)
                if form.is_valid():
                    form.save()  # Actualizar el artículo
                    mensaje = "Región actualizada correctamente."
                    lista_region = Region.objects.all()
                    context = {
                        "form": form,
                        "articulo": region,
                        "regions": lista_region,
                        "mensaje": mensaje,
                    }
                    return render(request, 'ventas/Articulos_edit.html', context)

            else:
                form = RegionForm(instance=region)
                lista_region = Region.objects.all()
                context = {
                    "form": form,
                    "articulo": region,
                    "regions": lista_region,
                }
                return render(request, 'ventas/Articulos_edit.html', context)
    except Region.DoesNotExist:
        mensaje = "El artículo no existe."
        lista_region = Region.objects.all() 
        context = {
            "mensaje": mensaje,
            "regions": lista_region,
        }
        return render(request, 'ventas/Articulos_list.html', context)

