from django.contrib import admin

from .models import StoreAccount, WarehouseOrder


@admin.register(StoreAccount)
class StoreAccountAdmin(admin.ModelAdmin):
    readonly_fields = ('token',)


@admin.register(WarehouseOrder)
class WarehouseOrderAdmin(admin.ModelAdmin):
    readonly_fields = ('number', 'created', 'updated', 'store_account')

    def has_add_permission(self, request, obj=None):
        return False
