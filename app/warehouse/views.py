from rest_framework import generics

from .serializers import WarehouseOrderSerializer


class WarehouseOrderCreateView(generics.CreateAPIView):
    serializer_class = WarehouseOrderSerializer
