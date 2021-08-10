from servicios.models import Servicio
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from .formulario import FormularioServicio
from .models import Servicio

# Create your views here.
def servicio(request):
    servicio = FormularioServicio()
    if request.method == "POST":
        servicio = FormularioServicio(request.POST)
        if servicio.is_valid():
            servicio.save()
            # Datos para mandar correo
            tipo = request.POST["tipo"]
            descripcion = request.POST["descripcion_envio"]
            nombre = request.POST["nombre_receptor"]
            direccion = request.POST["direccion_receptor"]
            correo(tipo,descripcion,nombre,direccion)
            return render(request,"servicio.html",{"servicio":tipo})
    return render(request,"servicio.html",{"form":servicio})

def correo(tipo,descripcion,nombre,direccion):
    diccionario = {"nombre":nombre,"direccion":direccion,"tipo":tipo,"descripcion":descripcion}
    plantilla = get_template("solicitud.html")
    body = plantilla.render(diccionario)
    enviar = EmailMultiAlternatives(
            "[usuario] ha realizado una solicitud" # subject
            ,"body" # body
            ,"josea.vazquez@edu.uag.mx" # sender
            ,[nombre] # receiver
            ,["jrendon@edu.uag.mx"] # cc
        )
    enviar.attach_alternative(body,"text/html")
    enviar.send()
    return HttpResponse("Hola")

class ListaServicios(generic.ListView):
    model = Servicio
    context_object_name = "servicios" 
    template_name = "ListaSolicitudes.html"