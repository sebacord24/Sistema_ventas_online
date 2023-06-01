from django.urls import path
from .views import HomeView, product, mantencion, reparacion



urlpatterns = [
    path('', HomeView, name='home'),
    path('product/', product, name='product'),
    path('mantencion/', mantencion, name='mantencion'),
    path('reparacion/', reparacion, name='reparacion'),


]