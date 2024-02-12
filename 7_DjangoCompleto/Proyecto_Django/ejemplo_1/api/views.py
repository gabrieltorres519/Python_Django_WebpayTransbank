from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, HttpResponse

class Class_Test(APIView):
    
    # Petición vía GET
    def get(self, request):
        #return Response({"mensaje": "Hola desde mi API"}) #envío de JSON
        return HttpResponse("Datos de respuesta")