from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductFileSerializer

# -------------------------------
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductFileSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductFileSerializer(products, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def product_create(request):
    serializer = ProductFileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def product_edit(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductFileSerializer(products, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def product_delete(request, pk):
    products = Product.objects.get(id=pk)
    products.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




