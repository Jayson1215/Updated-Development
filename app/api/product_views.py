# product_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Product
from .product_serialize import ProductSerializer

class ProductDetailView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise NotFound("Product not found")
        
        serializer = ProductSerializer(product)
        return Response(serializer.data)
