from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Servicio(models.Model):
    tipo = models.CharField(max_length=100, choices=[("mensajeria","Mensajería"),("paqueteria","Paquetería")])
    descripcion_envio = models.CharField(max_length=250)
    nombre_receptor = models.CharField(max_length=100)
    direccion_receptor = models.CharField(max_length=100)
