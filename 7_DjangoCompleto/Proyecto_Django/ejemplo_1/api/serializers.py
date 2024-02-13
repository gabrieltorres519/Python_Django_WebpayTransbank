from rest_framework import serializers
from home.models import *


class ProductoSerializer(serializers.ModelSerializer):
	categoria = serializers.CharField(source='categoria.nombre') # Debido a que es una llave foránea debemos especificar para mostrar la info
	foto = serializers.ImageField(use_url=False) # Para solo almacenar el nombre del archivo sin el nombre de la carpeta en la que se encuentra
	class Meta:
		model = Producto
		fields = ("id", "categoria", "categoria_id", "nombre", "descripcion", "foto", "fecha")


# class ProductoSaveSerializer(serializers.ModelSerializer):
	
# 	class Meta:
# 		model = Producto
# 		fields = "__all__"


# 	def create(self, validated_data):
# 		return Producto.objects.create(**validated_data)


class CategoriaSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Categoria
		fields = "__all__"