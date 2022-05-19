from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

from .forms import PersonalFormulario

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
    if request.method == 'POST':

        mi_formulario = PersonalFormulario(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            cuenta = informacion['cuenta']
            sector = informacion['sector']
            nombre = informacion['nombre']
            apellido = informacion['apellido']
            dni = informacion['dni']
            email = informacion['email']

            personalNuevo = Personal(cuenta=cuenta, sector=sector, nombre=nombre, apellido=apellido, dni=dni, email=email)

            personalNuevo.save()

            return render(request, 'AppExptes/inicio.html')

    else:

        mi_formulario = PersonalFormulario()

    return render(request, 'AppExptes/personalFormulario.html', {'miForm': mi_formulario})

