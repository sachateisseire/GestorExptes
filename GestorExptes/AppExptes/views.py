from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

def inicio(self):
    miHtml = open('C:\\Users\\Oficina\\Desktop\\GestorExptes\\GestorExptes\\AppExptes\\templates\\AppExptes\\inicio.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    return HttpResponse(plantilla.render(miContexto))

def personal(self):
    miHtml = open('C:\\Users\\Oficina\\Desktop\\GestorExptes\\GestorExptes\\AppExptes\\templates\\AppExptes\\personal.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    return HttpResponse(plantilla.render(miContexto))

def expedientes(self):
    miHtml = open('C:\\Users\\Oficina\\Desktop\\GestorExptes\\GestorExptes\\AppExptes\\templates\\AppExptes\\expedientes.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    return HttpResponse(plantilla.render(miContexto))

def sector(self):
    miHtml = open('C:\\Users\\Oficina\\Desktop\\GestorExptes\\GestorExptes\\AppExptes\\templates\\AppExptes\\sector.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    return HttpResponse(plantilla.render(miContexto))