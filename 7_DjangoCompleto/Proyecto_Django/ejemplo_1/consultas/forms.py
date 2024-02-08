from django import forms
from utilidades import formularios
from home.models import *


class Formulario_producto(forms.Form):
	nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'autocomplete':'off'}))
	precio = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Precio', 'onkeypress': 'return soloNumeros(event)', 'autocomplete':'off'}))
	categoria=forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control '}), choices=formularios.get_categorias_choices)
	descripcion = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 3, 'cols': 100, 'class': 'form-control', 'placeholder': 'Descripción', 'id': 'mensaje', 'autocomplete':'off'}))
	file = forms.CharField(required=False, widget=forms.TextInput(attrs={ 'type': 'file', 'id':'formFile', 'class': 'form-control'}))

class Formulario_atributo_producto(forms.Form):
	atributos = forms.CharField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'f  ss'}, choices=Atributo.objects.all().values_list('id', 'nombre'))
     )
	
