from django.db import models

# Create your models here.
class Blogs(models.Model):
    titulo=models.CharField(max_length=30)
    autor=models.CharField(max_length=30)
    fecha=models.DateField()
    contenido=models.CharField(max_length=800)
    