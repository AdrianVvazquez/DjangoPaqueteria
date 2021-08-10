from django import forms
from servicios.models import Servicio

class FormularioServicio(forms.ModelForm):
    class Meta:
        model= Servicio
        fields= ["tipo","descripcion_envio","nombre_receptor","direccion_receptor"]
