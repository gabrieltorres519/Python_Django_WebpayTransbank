from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, HttpResponse
from utilidades import utilidades
from home.models import *
from django.contrib.auth import authenticate, login
import time

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
     
     
class Class_TestRequest(APIView):
	
	#pasar parámetros vía json request
	def post(self, request):
		data=request.data
		return Response({"manzana": data.get('correo')})
      

class Class_TestLogin(APIView):
	
	"""
	request: {"correo":"info@tamila.cl", "password":"123456"}
	"""
	def post(self, request):
		data=request.data
		if data.get("correo") == None or data.get("password") == None:
			raise Http404
		user = authenticate(request, username=data.get("correo"), password=data.get("password"))
		if user is not None:
			login(request, user)
			usersMetadata = UsersMetadata.objects.filter(user_id=request.user.id).get()
			nombre=f"{request.user.first_name} {request.user.last_name}"
			token=utilidades.getToken({"id":request.user.id, "campo":"hola", 'time':int(time.time())})
			data_json={"mensaje":"ok", "nombre":nombre, "token":token}
			return Response(data_json)
		else:
			return Response({"mensaje":"Los datos ingresados no son correctos"})