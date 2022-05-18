from django.urls import path
from AppExptes.views import expedientes, inicio, personal, sector


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('personal/', personal, name='Personal'),
    path('expedientes/', expedientes, name='Expedientes'),
    path('sector/', sector, name='Sector'),
]