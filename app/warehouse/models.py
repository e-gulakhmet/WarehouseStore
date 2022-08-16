import binascii
import os

from django.db import models

from orders.models import OrderBaseModel
from accounts.models import AccountBaseModel


class StoreAccount(AccountBaseModel):
    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_token()
        return super().save(*args, **kwargs)

    @staticmethod
    def generate_token():
        token = binascii.hexlify(os.urandom(20)).decode()
        return StoreAccount.generate_token() if StoreAccount.objects.filter(token=token).exists() else token


class WarehouseOrder(OrderBaseModel):
    store_account = models.ForeignKey(StoreAccount, on_delete=models.RESTRICT, related_name='orders',
                                      null=True, blank=False)

    def __str__(self):
        return f'Order {self.number}: {self.get_status_display()} | Warehouse [{self.store_account.name}]'
