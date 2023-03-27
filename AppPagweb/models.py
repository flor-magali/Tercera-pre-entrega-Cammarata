from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Email = models.EmailField()
    Direccion = models.CharField(max_length=40)
     
    def __str__(self):
        return f"{self.id} - {self.Nombre}"
    
class Postear(models.Model):
    Titulo = models.CharField(max_length=60)
    Animal = models.CharField(max_length=40)
    Caracteristicas = models.CharField(max_length=150)
    Mensaje = models.CharField(max_length=100)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
    image = models.ImageField(upload_to="posts", null=True, blank=True)

    @property
    def image_url(self):
        return self.image.url if self.image else ''

    def __str__(self):
        return f"{self.id} - {self.Animal}"

class Adoptame(models.Model):
    Animal = models.CharField(max_length=40)
    Caracteristicas = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.id} - {self.Animal}"