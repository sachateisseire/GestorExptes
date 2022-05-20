from django.urls import path
from AppExptes.views import expedientes, inicio, personal, sector, personalFormulario, sectorFormulario, expedientesFormulario, busquedaSector, buscar, leerSector, eliminarSector

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('personal/', personal, name='Personal'),
    path('expedientes/', expedientes, name='Expedientes'),
    path('sector/', sector, name='Sector'),
    path('personalFormulario/', personalFormulario, name='PersonalFormulario'),
    path('sectorFormulario/', sectorFormulario, name='SectorFormulario'),
    path('expedientesFormulario/', expedientesFormulario, name='ExpedientesFormulario'),
    path('busquedaSector/', busquedaSector, name='BusquedaSector'),
    path('busqueda/', buscar, name='Buscar'),
    path('leerSector/', leerSector, name="LeerSector"),
    path('eliminarSector/<id>', eliminarSector, name='EliminarSector'),
]