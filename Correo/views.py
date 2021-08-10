from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import get_template

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def inicio(request):
    return render(request,"inicio.html")

def registroUsuario(request):
    f = UserCreationForm()
    if request.method == "POST":
        f = UserCreationForm(data = request.POST)
        if f.is_valid():
            usr = f.save()
            a = "¡Bienvenido!"
            return render(request,"login.html",{"h":a})

    f.fields["username"].help_text = None
    f.fields["password1"].help_text = None
    f.fields["password2"].help_text = None
    return render(request,"nuevoUsuario.html",{"formulario":f})
# login
def ingresar(request):
    f = AuthenticationForm()
    if request.method == "POST":
        f = AuthenticationForm(data = request.POST)
        if f.is_valid():
            u = request.POST["username"]
            name = request.POST["username"]
            p = request.POST["password"]
            usr = authenticate(username = u, password = p)
            if usr is not None:
                login(request, usr)
                # llave de usuario
                request.session["variableSesion"] = u
                return render(request,"inicio.html")
    return render(request,"login.html",{"formulario":f})
# logout
def salir(request):
    logout(request)
    return redirect("/login")