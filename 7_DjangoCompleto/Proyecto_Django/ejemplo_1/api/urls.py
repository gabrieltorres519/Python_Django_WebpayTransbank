from django.urls import path
from django.conf.urls import  url
from .views import *


urlpatterns = [
	#api/v1/test endpoint
	path('/test', Class_Test.as_view(), name="api_test"),
	path('/test-parametro/<int:id>', Class_TestParametro.as_view(), name="api_test_parametro"),
	path('/test-request', Class_TestRequest.as_view(), name="api_test_parametro"),
	path('/test-login', Class_TestLogin.as_view(), name="api_test_login"),
	path('/test-jwt', Class_TestJwt.as_view(), name="api_test_jwt"),
	path('/test-crear-registros', Class_TestCrearRegistros.as_view(), name="api_test_jwt"),
	path('/test-serializable', Class_TestSerializable.as_view(), name="api_test_serializable"),
	path('/test-productos', Class_TestProductos.as_view(), name="api_test_Productos"),
]