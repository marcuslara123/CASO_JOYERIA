from django.shortcuts import render

# Create your views here.

def inicio(request):
    context={}
    return render (request, 'venta/index.html',context)


def anillos(request):
    context = {}
    return render(request, 'venta/Anillos.html', context)

def registrojs(request):
    context = {}
    return render(request, 'venta/RegistroJS.html', context)