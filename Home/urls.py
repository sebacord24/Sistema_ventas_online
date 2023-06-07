from django.urls import path
from .views import *



urlpatterns = [
    path('', HomeView, name='home'),
    path('admin/', admin, name='admin'),
    path('product/', product, name='product'),
    path('mantencion/', ListarMante, name='mantencion'),
    path('reparacion/', reparacion, name='reparacion'),
    path('filtro_libros_nombre/', filtro_libros_nombre, name='filtro_libros_nombre'),
    path('mantencion/agregar_mantenimiento/', agregar_mantenimiento, name='agregar_mantenimiento'),
    path('checkout/', checkout_view, name='checkout'),
    path('eliminar_del_carrito/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('agregar_al_carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('detalle_carrito/', detalle_carrito, name='detalle_carrito'),
    path('autenticar_usuario/', autenticar_usuario, name='autenticar_usuario'),
    path('login/', Login, name='login'),
    path('clientes_form/', clientes_form, name='clientes_form'),
    path('agregar_cliente/', agregar_cliente, name='agregar_cliente'),
]




