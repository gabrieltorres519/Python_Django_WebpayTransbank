from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, HttpResponse
from utilidades import utilidades
from home.models import *
from django.contrib.auth import authenticate, login
import time
from jose import jwt
from django.conf import settings

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
		

class Class_TestJwt(APIView):
	
	# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiY2FtcG8iOiJob2xhIiwidGltZSI6MTcwNzc2ODIzMX0.BGf4wmZaupipBMKbdtM3srKEvRlZSjBteS1dBw38-PE
	def get(self, request):
		headers = request.headers.get('Authorization')
		if not headers:
			res = HttpResponse("Unauthorized")
			res.status_code = 401
			return res

		try:
			resuelto = jwt.decode(headers, settings.SECRET_KEY, algorithms=['HS256'])
		except Exception as e:
			res = HttpResponse("Unauthorized")
			res.status_code=401
			return res
		print("El campo resuelto es: " + resuelto["campo"])
		if not resuelto['campo']=="hola":
			res = HttpResponse("Unauthorized")
			res.status_code=401
			return res
		data=request.data
		return Response({"manzana": resuelto})
	

class Class_TestCrearRegistros(APIView):
	
	
	def post(self, request):
		headers = request.headers.get('Authorization')
		if not headers:
			res = HttpResponse("Unauthorized")
			res.status_code = 401
			return res

		try:
			resuelto = jwt.decode(headers, settings.SECRET_KEY, algorithms=['HS256'])
		except Exception as e:
			res = HttpResponse("Unauthorized")
			res.status_code=401
			return res
		
		if not resuelto['campo']=="hola":
			res = HttpResponse("Unauthorized")
			res.status_code=401
			return res
		data=request.data
		cat=Categoria.objects.create(nombre=data['nombre'])
		return Response({"mensaje": f"se creó la categoría {cat.id}"})