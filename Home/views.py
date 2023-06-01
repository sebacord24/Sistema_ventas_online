from multiprocessing import connection
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def HomeView(request):
    libros = Libro.objects.all()
    data = {  
        'libros': libros    
    }
    print(libros)
    return render(request, 'Home/index.html', data)

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

def listado_libros():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("listarlibros", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_libros_busqueda_nombre(busqueda):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("listarlibros_busqueda_nombre", [out_cur,busqueda])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_libros_busqueda_categoria(busqueda):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("listarlibros_busqueda_categoria", [out_cur,busqueda])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def filtro_libros_nombre(request):
    busqueda = "nombre_libro"  # Aquí puedes establecer el valor de búsqueda que necesites
    lista = listado_libros_busqueda_nombre(busqueda)
    return render(request, 'lista_libros.html', {'libros': lista})

def filtro_libros_categoria(request):
    busqueda = "categoria"  # Aquí puedes establecer el valor de búsqueda que necesites
    lista = listado_libros_busqueda_nombre(busqueda)
    return render(request, 'lista_libros.html', {'libros': lista})
