from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import WarehouseOrder
from .serializers import WarehouseOrderSerializer

from orders.services import OrdersSyncService


@receiver(post_save, sender=WarehouseOrder)
def store_order_post_save_handler(sender, instance: WarehouseOrder, created: bool, **kwargs):
    if created:
        return
    OrdersSyncService().update_order(instance, WarehouseOrderSerializer, instance.store_account)
