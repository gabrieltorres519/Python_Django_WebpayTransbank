from django import forms


class Formulario_importar_excel(forms.Form):
	file = forms.FileField(required=False, 
        widget=forms.FileInput(
            attrs={'class': 'ss', 'id': 'file', 'data-min-file-count': '1'}
            )
        )


class Formulario_importar_txt(forms.Form):
	file = forms.FileField(required=False, 
        widget=forms.FileInput(
            attrs={'class': 'ss', 'id': 'file', 'data-min-file-count': '1'}
            )
        )