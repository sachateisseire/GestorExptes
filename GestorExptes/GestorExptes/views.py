from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

def saluda2(self):
    miHtml = open('C:\\Users\\Oficina\\Desktop\\GestorExptes\\GestorExptes\\AppExptes\\templates\\AppExptes\\padre.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    return HttpResponse(plantilla.render(miContexto))