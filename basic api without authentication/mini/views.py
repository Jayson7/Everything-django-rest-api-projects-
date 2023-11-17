# views.py

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products
from .serializers import ProductSerializer

class ProductListView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
