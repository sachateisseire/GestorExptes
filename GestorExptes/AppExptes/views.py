from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

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