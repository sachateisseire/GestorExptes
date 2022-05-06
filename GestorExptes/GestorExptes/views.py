from django.http import HttpResponse
from django.template import Context, Template

def saluda2(self):
    miHtml = open('C:\\Users\\Oficina\\Desktop\\GestorExptes\\GestorExptes\\GestorExptes\\templates\\template.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    return HttpResponse(plantilla.render(miContexto))