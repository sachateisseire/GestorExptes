from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Personal(models.Model):
    cuenta = models.CharField('cuenta', max_length=30)
    sector = models.CharField('sector', max_length=30)
    nombre = models.CharField('nombre', max_length=30)
    apellido = models.CharField('apellido', max_length=30)
    dni = models.IntegerField('dni')
    email = models.CharField('email', max_length=50)

    def __str__(self) -> str:
        return f'{self.cuenta}'

class Expediente(models.Model):
    numero = models.CharField('numero', max_length=50)
    tipo = models.CharField('tipo', max_length=50)
    fechaDeEntrada = models.CharField('fecha_de_entrada', max_length=50)
    estado = models.CharField('estado', max_length=50)
    cuenta = models.CharField('cuenta', max_length=30)

    def __str__(self) -> str:
        return f'{self.numero}'    

class Sector(models.Model):
    nombre = models.CharField('nombre', max_length=30)
    sectorCoordinador = models.CharField('sector_coordinador', max_length=30)

    def __str__(self) -> str:
        return f'{self.nombre} - {self.sectorCoordinador}'

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
