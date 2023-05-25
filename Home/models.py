from django.db import models

# Create your models here.

class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    editorial = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="libros", null=True)

    def __str__(self):
        return self.nombre