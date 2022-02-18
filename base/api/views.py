from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializers

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.products.all()
    serializer_class = ProductSerializers

