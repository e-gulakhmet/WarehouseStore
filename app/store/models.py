from django.db import models

from utils.models import OrderBaseModel, AccountBaseModel


class WarehouseAccount(AccountBaseModel):
    pass


class StoreOrder(OrderBaseModel):
    warehouse_account = models.ForeignKey(WarehouseAccount, on_delete=models.SET_NULL, related_name='orders',
                                          null=True, blank=False)

    def __str__(self):
        return f'Order [{self.number} - {self.get_status_display()}] Warehouse [{self.warehouse_account.name}]'
