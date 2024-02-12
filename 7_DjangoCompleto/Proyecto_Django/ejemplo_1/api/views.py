from rest_framework.views import APIView
from rest_framework.response import Response


class Class_Test(APIView):
    
    # Petición vía GET
    def get(self, request):
        return Response({"mensaje": "Hola desde mi API"})