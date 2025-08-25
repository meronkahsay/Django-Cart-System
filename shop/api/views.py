from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from catalogue.models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
