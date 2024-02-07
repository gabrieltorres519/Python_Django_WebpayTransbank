from django import forms
from django.core import validators
from django.forms import PasswordInput


class Formulario_Login(forms.Form):
    correo = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail', 'autocomplete':'off'}))
    password = forms.CharField(required=True, widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'autocomplete':'off'}))


class Formulario_ejemplo(forms.Form):
	nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre', 'autocomplete': 'off'}))
	correo = forms.CharField(required=True, 
		widget=forms.TextInput(
			attrs={'class': 'form-control', 'placeholder': 'E-Mail'}
			),
			validators=[
				validators.MinLengthValidator(4, message="El E-Mail es demasiado corto"),
				validators.RegexValidator('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', message="El E-Mail ingresado no es válido")
			],
			error_messages={'required':'El campo E-Mail está vacío' }
		)
	telefono = forms.CharField(required=True, widget=forms.TextInput(
			attrs={'class': 'form-control', 'placeholder': 'Teléfono', 'autocomplete':'off'}
			),
			validators=[
                validators.MinLengthValidator(4, message="El Teléfono es demasiado corto"),
                validators.RegexValidator('^[+0-9 ]*$', message="El Teléfono contiene caracteres inválidos, por favor use sólo números, por ejemplo +5691652132")
            ]
	)
	mensaje = forms.CharField(required=True, widget=forms.Textarea(
		attrs={'class': 'form-control', 'placeholder': 'Mensaje', 'rows': 5, 'cols': 100}
		),
		validators=[
			validators.MinLengthValidator(4, message="El Mensaje es demasiado corto"),
			validators.RegexValidator('^[A-Za-z0-9ñÑáéíóúäëïöüÁÉÍÓÚÄËÏÖÜ,. ]*$', message="El Mensaje contiene caracteres inválidos, por favor use sólo números y letras")
		]
	)