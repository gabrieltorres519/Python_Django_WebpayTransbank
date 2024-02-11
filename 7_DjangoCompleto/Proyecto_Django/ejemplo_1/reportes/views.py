from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
from django.template.loader import render_to_string
from weasyprint import HTML # pip intall WeasyPrint
import os

# Create your views here.
def reportes_inicio(request):
    # return HttpResponse("Hola mundo")
    return  render(request, 'reportes/home.html', {}) # contiene la ruta del template de esa vista y los datos que se quieren renderizar en la vista


def reportes_pdf(request):
    ruta = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_url = settings.BASE_URL
    template = f"{ruta}/templates/layout/ajax.html"
    texto="mi muñeca me habló"
    data = {'texto': texto, 'template':template, 'request': request, 'ruta': ruta, 'base_url': base_url}

    html = render_to_string(f"{ruta}/templates/reportes/pdf.html", data)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"]= "inline; mi_pdf.pdf"
    HTML(string=html).write_pdf(response)
    return response
