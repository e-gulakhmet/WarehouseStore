from django.urls import path
from rest_framework import routers

from .views import *

app_name = 'Warehouse api'

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    path('orders', WarehouseOrderCreateView.as_view(), name='warehouse-order-create'),
]

urlpatterns += router.urls
