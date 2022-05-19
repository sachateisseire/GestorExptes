from django import forms

class PersonalFormulario(forms.Form):

    cuenta = forms.CharField()
    sector = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    email = forms.CharField()