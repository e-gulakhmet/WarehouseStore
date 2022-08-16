from django.db import models

from orders.models import OrderBaseModel
from accounts.models import AccountBaseModel


class WarehouseAccount(AccountBaseModel):
    pass


class StoreOrder(OrderBaseModel):
    warehouse_account = models.ForeignKey(WarehouseAccount, on_delete=models.RESTRICT, related_name='orders',
                                          null=True, blank=False)

    def __str__(self):
        return f'Order {self.number}: {self.get_status_display()} | Warehouse: [{self.warehouse_account}]'
