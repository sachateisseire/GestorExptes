from django.urls import path
from AppExptes.views import expedientes, inicio, personal, sector, personalFormulario, personalFormularioPost


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('personal/', personal, name='Personal'),
    path('expedientes/', expedientes, name='Expedientes'),
    path('sector/', sector, name='Sector'),
    path('personalFormulario/', personalFormulario, name='PersonalFormulario'),
    path('personalFormularioPost/', personalFormularioPost, name='PersonalFormularioPost')
]