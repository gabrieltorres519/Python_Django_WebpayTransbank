from django.core.paginator import Paginator
from django.conf import settings
import os
# import jwt


# def getToken(json):
#     token= jwt.encode(json, settings.SECRET_KEY, algorithm='HS256')
#     return token



def get_paginacion(total, request):
	page = request.GET.get('page') # Se recibe el número de página de la utl (querystring)
	paginator = Paginator(total, settings.TOTAL_PAGINAS) # Al método paginator de Django se le pasan todos los productos y el total de páginas en que se van a paginar
	datos = paginator.get_page(page) # Obteniendo los datos solo de la página seleccionada
	numeros=[]
	if len(datos)>=settings.TOTAL_PAGINAS:
		for ultima in range(1, datos.paginator.num_pages):
			numeros.append(ultima)
		numeros.append(ultima+1)

	return [datos, numeros, int(page)]


def getExtension(file):
    extension = os.path.splitext(str(file))[1]
    if extension == ".png":
        return True
    elif extension == ".jpg":
        return True
    elif extension == ".jpeg":
        return True
    elif extension == ".JPG":
        return True
    elif extension == ".PNG":
        return True
    elif extension == ".JPEG":
        return True
    else:
        return False


def getExtensionSoloPdf(file):
    extension = os.path.splitext(str(file))[1]
    if extension == ".pdf":
        return True
    else:
        return False