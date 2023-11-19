# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products
from .serializers import ProductSerializer

class ProductListView(APIView):
    def get(self, request, *args, **kwargs):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ProductDetailView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        product.delete_product()
        return Response(status=status.HTTP_204_NO_CONTENT)