from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

from .models import Personal

def inicio(request):
    return render(request, 'AppExptes/inicio.html')

def personal(request):
    return render(request, 'AppExptes/personal.html')

def expedientes(request):
    return render(request, 'AppExptes/expedientes.html')

def sector(request):
    return render(request, 'AppExptes/sector.html')

def personalFormulario(request):
    return render(request, 'AppExptes/personalFormulario.html')

def personalFormulario(request):
    return render(request, 'AppExptes/personalFormulario.html')

def personalFormularioPost(request):

    cuenta = request.POST['cuenta']
    sector = request.POST['sector']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    dni = request.POST['dni']
    email = request.POST['email']

    personalNuevo = Personal(cuenta=cuenta, sector=sector, nombre=nombre, apellido=apellido, dni=dni, email=email)

    personalNuevo.save()

    return render(request, 'AppExptes/personal.html')
