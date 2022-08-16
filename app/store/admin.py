from django.contrib import admin

from .models import WarehouseAccount, StoreOrder


@admin.register(WarehouseAccount)
class WarehouseAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(StoreOrder)
class StoreOrderAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return 'number', 'status', 'warehouse_account', 'created', 'updated'
        return super().get_readonly_fields(request, obj)
