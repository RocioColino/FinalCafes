from django.db import models

# Create your models here.
class Blogs(models.Model):
    titulo=models.CharField(max_length=30)
    subtitulo=models.CharField(max_length=40)
    autor=models.CharField(max_length=30)
    fecha=models.DateField()
    imagen=models.ImageField()
    cuerpo=models.CharField(max_length=800)
class Cafeterias(models.Model):
    nombre=models.CharField(max_length=30)
    precio=models.IntegerChoices((1, "$"),(2, "$$"),(3, "$$$"),(4, "$$$$"))
    direccion=models.CharField(max_length=40)
    telefono=models.IntegerField()

    
