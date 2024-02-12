from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
from django.template.loader import render_to_string
from weasyprint import HTML # pip intall WeasyPrint
import os
from .forms import *
from django.core.files.storage import FileSystemStorage
import xlrd # pip install xlrd | pip install django excel

# Create your views here.
def reportes_inicio(request):
    # return HttpResponse("Hola mundo")
    return  render(request, 'reportes/home.html', {}) # contiene la ruta del template de esa vista y los datos que se quieren renderizar en la vista

def reportes_importar_excel(request):
    # return HttpResponse("Hola mundo")
    if request.method == 'POST':
        form = Formulario_importar_excel(request.POST,request.FILES)
        if form.is_valid():
            datos = form.cleaned_data
            fs = FileSystemStorage()
            filename=fs.save(f"excel/archivo.xlsx",request.FILES['file'])
            upload_file_url=fs.url(filename)

            #leer el archivo
            documento=xlrd.open_workbook(settings.BASE_DIR + "/media/excel/archivo.xls")
            datos = documento.sheet_by_index(0)
			#guardar el la bd la información
            for i in range(datos.nrows):
                if i>=1:
					#repr(datos.cell_value(i, 0)).replace("'","")
                    Nombres.objects.create(numero=repr(datos.cell_value(i, 0)).replace("'",""), nombre=repr(datos.cell_value(i, 1)).replace("'",""))
            remove(settings.BASE_DIR+'/media/excel/archivo.xls')
        messages.add_message(request, messages.SUCCESS, f"El excel se importó exitosamente")
        return HttpResponseRedirect(f"/reportes/importar-excel")
    else:
        form = Formulario_importar_excel()

    return  render(request, 'reportes/importar_excel.html', {'form':form}) 

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
