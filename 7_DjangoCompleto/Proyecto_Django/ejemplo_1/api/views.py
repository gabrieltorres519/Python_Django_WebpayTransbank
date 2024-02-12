from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, HttpResponse

class Class_Test(APIView):
    
    # Petición vía GET
    def get(self, request):
        #return Response({"mensaje": "Hola desde mi API"}) #envío de JSON
        #res =HttpResponse("Datos de respuesta")
        #res.status_code=401
		#return res
        return Response({"mensaje": "hola desde mi api con ñandú"})
    
    def post(self, request):

        return Response({"mensaje": "respuesta post"})


    def put(self, request):

        return Response({"mensaje": "respuesta put"})


    def delete(self, request):

        return Response({"mensaje": "respuesta delete"})


class Class_TestParametro(APIView):
	
	
	def get(self, request, id):
		
		return Response({"mensaje": f"id={id}"})