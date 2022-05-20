from django.urls import path
from django.contrib.auth.views import LogoutView
from AppExptes.views import avatar2, faqs, about1, about2, ExpedientesLista, ExpedientesCreacion, ExpedientesDelete, ExpedientesDetalle, ExpedientesUpdate, SectorCreacion, SectorDelete, SectorDetalle, SectorLista, SectorUpdate, PersonalLista, PersonalCreacion, PersonalDelete, PersonalDetalle, PersonalUpdate, inicio, personalFormulario, sectorFormulario, expedientesFormulario, busquedaSector, buscar, leerSector, eliminarSector, editarSector, loginView, register, editar_perfil



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
    path('sector/lista/', SectorLista.as_view(), name='SLista' ),
    path('sector/detail/<pk>', SectorDetalle.as_view(), name='SDetail' ),
    path('sector/edit/<pk>', SectorUpdate.as_view(), name='SEdit' ),
    path('sector/delete/<pk>', SectorDelete.as_view(), name='SDelete' ),
    path('sector/create/', SectorCreacion.as_view(), name='SNew' ),
    path('sector/lista/', SectorLista.as_view(), name='SLista' ),
    path('expedientes/detail/<pk>', ExpedientesDetalle.as_view(), name='EDetail' ),
    path('expedientes/edit/<pk>', ExpedientesUpdate.as_view(), name='EEdit' ),
    path('expedientes/delete/<pk>', ExpedientesDelete.as_view(), name='EDelete' ),
    path('expedientes/create/', ExpedientesCreacion.as_view(), name='ENew' ),
    path('expedientes/lista/', ExpedientesLista.as_view(), name='ELista' ),
    path('login/', loginView, name='Login'),
    path('registrar/', register, name='Registrar'),
    path('logout/', LogoutView.as_view(template_name='AppExptes/logout.html'), name='Logout'),
    path('editarPerfil/', editar_perfil, name='EditarPerfil'),
    path('about2/', about2, name="About2"),
    path('about1/', about1, name="About1"),
    path('faqs/', faqs, name="Faqs"),
    path('avatares/', avatar2, name="Avatar"),

            
]