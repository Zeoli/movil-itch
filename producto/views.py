from django.shortcuts import render
from .models import *
# Create your views here.

def Main_view(request):
    productos = Producto.objects.all()
    productos = list(productos)
    return render(request, 'index.html', {'productos': productos})
