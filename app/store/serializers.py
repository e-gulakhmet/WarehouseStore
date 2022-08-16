from rest_framework import serializers

from .models import StoreOrder


class StoreOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreOrder
        fields = ('number', 'status')
        read_only_fields = ('number',)
