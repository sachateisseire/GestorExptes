from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .forms import ExpedientesFormulario, PersonalFormulario, SectorFormulario

from .models import Expediente, Personal, Sector

def inicio(request):
    return render(request, 'AppExptes/inicio.html')

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

def eliminarSector(request, id):

    sector = Sector.objects.get(id=id)

    sector.delete()

    sectores = Sector.objects.all()

    contexto = {"lista_sectores": sectores}

    return render(request, 'AppExptes/leerSector.html', contexto)

def editarSector(request, id):

    sector = Sector.objects.get(id=id)

    if request.method == 'POST':

        miFormulario = SectorFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            sector.nombre = informacion['nombre']
            sector.sectorCoordinador = informacion['sectorCoordinador']

            sector.save()

            return render(request, 'AppExptes/inicio.html')

    else:

        miFormulario = SectorFormulario(
            initial={
                'nombre': sector.nombre,
                'sectorCoordinador': sector.sectorCoordinador,
            }
        )
    
    return render(request, 'AppExptes/editarSector.html', {"miFormulario": miFormulario, "sector_nombre": sector.nombre})

class PersonalLista(ListView):

    model = Personal
    template_name = 'AppExptes/personal_lista.html'

class PersonalDetalle(DetailView):

    model = Personal
    template_name = 'AppExptes/personal_detalle.html'

class PersonalCreacion(CreateView):

    model = Personal
    success_url = '/AppExptes/personal/lista'
    fields = ['cuenta', 'sector', 'nombre', 'apellido', 'dni', 'email']

class PersonalUpdate(UpdateView):

    model = Personal
    success_url = '/AppExptes/personal/lista'
    fields = ['cuenta', 'sector', 'nombre', 'apellido', 'dni', 'email']

class PersonalDelete(DeleteView):

    model = Personal
    success_url = '/AppExptes/personal/lista'

def loginView(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            datos = form.cleaned_data

            usuario = datos['username']
            psw = datos['password']

            user = authenticate(username=usuario, password=psw)

            if user:

                login(request, user)

                return render(request, "AppExptes/inicio.html", {"mensaje": f'Bienvenido {usuario}'})

            else:

                return render(request, "AppExptes/inicio.html", {"mensaje": 'Datos incorrectos'})

        else:

            return render(request, "AppExptes/inicio.html", {"mensaje": 'Datos incorrectos'} )

    else:

        form = AuthenticationForm()

    return render(request, "AppExptes/login.html", {'form': form})

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']

            form.save()

            return render(request, "AppExptes/inicio.html", {'mensaje': f'Usuario {username} creado'})

    else:

        form = UserCreationForm()

    return render(request, "AppExptes/registro.html", {'form': form})