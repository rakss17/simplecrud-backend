from django.shortcuts import render
from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializers


class ProductsListCreateView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


class ProductsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
