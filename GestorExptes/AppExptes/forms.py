from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PersonalFormulario(forms.Form):

    cuenta = forms.CharField()
    sector = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    email = forms.CharField()

class SectorFormulario(forms.Form):

    nombre = forms.CharField()
    sectorCoordinador = forms.CharField()

class ExpedientesFormulario(forms.Form):

    numero = forms.CharField() 
    tipo = forms.CharField() 
    fechaDeEntrada = forms.CharField()
    estado = forms.CharField()
    cuenta = forms.CharField()

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label='Modificar email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {k:"" for k in fields}