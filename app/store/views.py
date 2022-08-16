from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import StoreOrder
from .serializers import StoreOrderSerializer


class StoreOrderUpdateView(generics.UpdateAPIView):
    serializer_class = StoreOrderSerializer
    queryset = StoreOrder.objects.all()
    http_method_names = ['patch']

    def get_object(self):
        return get_object_or_404(self.get_queryset(), number=self.kwargs['number'])
