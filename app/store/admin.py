from django.contrib import admin

from .models import StoreOrder, WarehouseAccount


@admin.register(WarehouseAccount)
class WarehouseAccountAdmin(admin.ModelAdmin):
    readonly_fields = ('token',)


@admin.register(StoreOrder)
class StoreOrderAdmin(admin.ModelAdmin):
    pass
