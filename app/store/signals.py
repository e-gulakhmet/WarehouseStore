from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import StoreOrder
from .serializers import StoreOrderSerializer

from orders.services import OrdersSyncService


@receiver(post_save, sender=StoreOrder)
def store_order_post_save_handler(sender, instance: StoreOrder, created: bool, **kwargs):
    if not created:
        return

    OrdersSyncService().create_order(instance, StoreOrderSerializer, instance.warehouse_account)
