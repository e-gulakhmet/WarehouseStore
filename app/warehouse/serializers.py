from rest_framework import serializers, exceptions

from .models import WarehouseOrder


class WarehouseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseOrder
        fields = ('status', 'number')

    def validate(self, attrs):
        attrs = super().validate(attrs)
        try:
            account = self.context['request'].account
        except AttributeError:
            raise exceptions.PermissionDenied('Account is not found. Check Account-Authorization header')
        attrs['store_account'] = account
        return attrs
