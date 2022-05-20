from django import forms

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