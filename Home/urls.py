from django.urls import path
from .views import HomeView, Register, Login, product, mantencion, reparacion

urlpatterns = [
    path('', HomeView, name='home'),
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('product/', product, name='product'),
    path('mantencion/', mantencion, name='mantencion'),
    path('reparacion/', reparacion, name='reparacion'),

]