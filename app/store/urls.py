from django.urls import path
from rest_framework import routers

from .views import *

app_name = 'Store api'

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    path('orders/<str:number>', StoreOrderUpdateView.as_view(), name='store-order-edit'),
]

urlpatterns += router.urls
