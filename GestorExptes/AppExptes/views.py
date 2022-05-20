from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

from .forms import ExpedientesFormulario, PersonalFormulario, SectorFormulario

from .models import Expediente, Personal, Sector

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

def sectorFormulario(request):
    if request.method == 'POST':

        mi_formulario = SectorFormulario (request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            nombre = informacion['nombre']
            sectorCoordinador = informacion['sectorCoordinador']

            sectorNuevo = Sector(nombre=nombre, sectorCoordinador=sectorCoordinador)

            sectorNuevo.save()

            return render(request, 'AppExptes/inicio.html')

    else:

        mi_formulario = SectorFormulario()

    return render(request, 'AppExptes/sectorFormulario.html', {'miForm': mi_formulario})


def expedientesFormulario(request):
    if request.method == 'POST':

        mi_formulario = ExpedientesFormulario (request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            numero = informacion['numero']
            tipo = informacion['tipo']
            fechaDeEntrada = informacion['fechaDeEntrada']
            estado = informacion['estado']
            cuenta = informacion['cuenta']

            expedienteNuevo = Expediente(numero=numero, tipo=tipo, fechaDeEntrada=fechaDeEntrada, estado=estado, cuenta=cuenta)

            expedienteNuevo.save()

            return render(request, 'AppExptes/inicio.html')

    else:

        mi_formulario = ExpedientesFormulario()

    return render(request, 'AppExptes/expedientesFormulario.html', {'miForm': mi_formulario})

def busquedaSector(request):

    return render(request, 'AppExptes/busquedaSector.html')

def buscar(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        sectorCoordinador = Sector.objects.filter(nombre=nombre)

        return render(request, 'AppExptes/resultadoBusquedaSector.html', {'nombre':nombre, 'sectorCoordinador':sectorCoordinador})

    else:

        return HttpResponse('Valor incorrecto')

def leerSector(request):

    sectores = Sector.objects.all()

    contexto = {'lista_sectores': sectores}

    return render(request, 'AppExptes/leerSector.html', contexto)

