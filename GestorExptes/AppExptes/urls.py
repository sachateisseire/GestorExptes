from django.urls import path
from AppExptes.views import PersonalLista, PersonalCreacion, PersonalDelete, PersonalDetalle, PersonalUpdate, inicio, personalFormulario, sectorFormulario, expedientesFormulario, busquedaSector, buscar, leerSector, eliminarSector, editarSector, loginView

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('personalFormulario/', personalFormulario, name='PersonalFormulario'),
    path('sectorFormulario/', sectorFormulario, name='SectorFormulario'),
    path('expedientesFormulario/', expedientesFormulario, name='ExpedientesFormulario'),
    path('busquedaSector/', busquedaSector, name='BusquedaSector'),
    path('busqueda/', buscar, name='Buscar'),
    path('leerSector/', leerSector, name="LeerSector"),
    path('eliminarSector/<id>', eliminarSector, name='EliminarSector'),
    path('editarSector/<id>', editarSector, name="EditarSector" ),
    path('personal/lista/', PersonalLista.as_view(), name='Lista' ),
    path('personal/detail/<pk>', PersonalDetalle.as_view(), name='Detail' ),
    path('personal/edit/<pk>', PersonalUpdate.as_view(), name='Edit' ),
    path('personal/delete/<pk>', PersonalDelete.as_view(), name='Delete' ),
    path('personal/create/', PersonalCreacion.as_view(), name='New' ),
    path('login/', loginView, name='Login'),           
]