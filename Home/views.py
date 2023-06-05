from django.db import connection, connections
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import base64
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from .models import *

# Create your views here.

def HomeView(request):
    data = {
        'libros': listado_libros()
    }
    return render(request, 'Home/index.html', data) 

def Register(request):
    return render(request, 'Home/register.html')
def Login(request):
    return render(request, 'Home/login.html')

def admin(request):
    return render(request, 'Home/admin.html')


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
        imagen = fila[8]
        if imagen is not None:
            imagen_data = str(base64.b64encode(imagen.read()), 'utf-8')
        else:
            imagen_data = None

        data = {
            'data': fila,
            'imagen': imagen_data
        }

        lista.append(data)

    return lista


def listado_libros_busqueda_nombre(busqueda):
    with connection.cursor() as cursor:
        cursor.callproc("listarlibros_busqueda_nombre", [busqueda])
        rows = cursor.fetchall()
        lista = [row[0] for row in rows]  # Modifica esto según la estructura de tus datos
    return lista

def listado_libros_busqueda_categoria(busqueda):
    with connection.cursor() as cursor:
        cursor.callproc("listarlibros_busqueda_categoria", [busqueda])
        rows = cursor.fetchall()
        lista = [row[0] for row in rows]  # Modifica esto según la estructura de tus datos
    return lista

def filtro_libros_nombre(request):
    busqueda = request.GET.get('busqueda', '')  # Obtener el término de búsqueda ingresado
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("listarlibros_busqueda_nombre", [out_cur, busqueda])

    libros = []
    for fila in out_cur:
        libros.append(fila)

    return render(request, 'Home/index.html', {'buscar': libros})

def filtro_libros_categoria(request):
    busqueda = "tipo_libro"  # Aquí puedes establecer el valor de búsqueda que necesites
    lista = listado_libros_busqueda_categoria(busqueda)
    return render(request, 'lista_libros.html', {'libros': lista})




def agregar_mantenimiento(request):
    if request.method == 'POST':
        id_mantencion = request.POST['id_mantencion']
        fec_mantencion = request.POST['fec_mantencion']

        # Obtener una conexión a la base de datos Oracle
        with connection.cursor() as cursor:
            # Ejecutar el procedimiento almacenado
            cursor.callproc('AGREGAR_MANTENIMIENTO', [id_mantencion, fec_mantencion])

    # Llamar a la función ListarMante para obtener la lista actualizada
    return ListarMante(request)

def ListarMante(request):
    # Obtener la lista de mantenciones
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LISTAR_SERVICIOS_MANTENCION", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    # Pasar la lista como contexto a la plantilla
    data = {
        'mantencion': lista
    }
    
    return render(request, 'Home/mantencion.html', data)









def obtener_o_crear_carrito(request):
    carrito = None
    if 'carrito_id' in request.session:
        carrito_id = request.session['carrito_id']
        try:
            carrito = Carrito.objects.get(id=carrito_id)
        except Carrito.DoesNotExist:
            pass
    if not carrito:
        carrito = Carrito.objects.create()
        request.session['carrito_id'] = carrito.id
    return carrito



def eliminar_del_carrito(request, item_id):
    try:
        item = ItemCarrito.objects.get(id=item_id)
        item.delete()
    except ItemCarrito.DoesNotExist:
        return HttpResponse("El item no existe en el carrito.")
    return redirect('detalle_carrito')

def agregar_al_carrito(request, producto_id=None):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
    if producto_id:
        try:
            producto = get_object_or_404(Libro, id=producto_id)
            carrito = obtener_o_crear_carrito(request)
            item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
            if not creado:
                item.cantidad += 1
                item.save()
        except Libro.DoesNotExist:
            return HttpResponse("El producto no existe.")
    return redirect('detalle_carrito')


def detalle_carrito(request):
    carrito = obtener_o_crear_carrito(request)
    items = ItemCarrito.objects.filter(carrito=carrito)
    total = 0  # Inicializar el total a cero
    if items:
        total = sum(item.producto.precio * item.cantidad for item in items)

    # Asignar los detalles del carrito
    carrito.detalles = "Detalles del carrito"

    return render(request, 'detalle_carrito.html', {'carrito': carrito, 'items': items, 'total': total})


def checkout_view(request):
    if request.method == 'POST':
        # Procesar los datos del formulario y realizar el pago
        # Guardar la información de la orden en la base de datos
        # Generar una confirmación de la orden
        return render(request, 'confirmacion.html', {'carrito': obtener_o_crear_carrito(request)})
    
    # Si es una solicitud GET, mostrar el formulario de checkout
    return render(request, 'Home/checkout.html')





def agregar_cliente(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        direccion = request.POST['direccion']
        rut = request.POST['rut']
        pr_nombre = request.POST['pr_nombre']
        seg_nombre = request.POST['seg_nombre']
        ap_paterno = request.POST['ap_paterno']
        ap_materno = request.POST['ap_materno']
        email = request.POST['email']
        fec_nac = request.POST['fec_nac']
        celular = request.POST['celular']
        password = request.POST['password']

        # Conectar a la base de datos Oracle
        with connection.cursor() as cursor:
            try:
                # Llamar al procedimiento almacenado
                cursor.callproc('sp_agregar_cliente', [
                    direccion, rut, pr_nombre, seg_nombre,
                    ap_paterno, ap_materno, email, fec_nac, celular, password
                ])
                messages.success(request, 'Cliente agregado exitosamente.')
            except Exception as e:
                error_message = str(e)
                if 'ORA-20001' in error_message:
                    messages.error(request, 'El rut ya está registrado.')
                else:
                    messages.error(request, 'Error al agregar el cliente. Por favor, inténtalo nuevamente.')

        # Redirigir a una página de éxito o mostrar un mensaje de éxito
        return redirect('clientes_form')

    # Renderizar el formulario de creación de cliente
    return render(request, 'Home/clientes_form.html')

def autenticar_usuario(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        password = request.POST.get('password')
        
        with connection.cursor() as cursor:
            try:
                resultado = cursor.var(int)
                cursor.callproc('autenticar_usuario', [rut, password, resultado])
                resultado = resultado.getvalue()
                
                if resultado == 1:
                    # Autenticación exitosa
                    messages.success(request, 'Inicio de sesión exitoso.')
                    return redirect('dashboard')
                elif resultado == 0:
                    # Autenticación fallida
                    messages.error(request, 'Credenciales inválidas. Inténtalo nuevamente.')
                else:
                    # Error en el procedimiento almacenado
                    messages.error(request, 'Error al autenticar el usuario. Por favor, inténtalo nuevamente.')
            except Exception as e:
                messages.error(request, 'Error al autenticar el usuario. Por favor, inténtalo nuevamente.')
                print(str(e))
    
    return render(request, 'Home/login.html')

