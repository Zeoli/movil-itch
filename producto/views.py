from django.shortcuts import render, redirect
from .models import Producto
# Create your views here.

def Main_view(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def GetProducto(request, id):
    try:
        producto = Producto.objects.get(pk=id)
    except Producto.DoesNotExist:
        msg = {'error': 'El producto no existe'}
        return redirect('/error', msg)
    return render(request, 'producto.html', {'producto': producto})