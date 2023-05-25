from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def HomeView(request):
    libros = Libro.objects.all()
    print(libros)
    return render(request, 'Home/index.html', {'libros': libros})

def Register(request):
    return render(request, 'Home/register.html')

def Login(request):
    return render(request, 'Home/login.html')

def product(request):
    return render(request, 'Home/product.html')

def mantencion(request):
    return render(request, 'Home/mantencion.html')

def reparacion(request):
    return render(request, 'Home/reparacion.html')
