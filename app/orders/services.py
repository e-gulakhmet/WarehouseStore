from typing import Type

import requests
from requests import Response
from rest_framework.serializers import Serializer

from .models import OrderBaseModel

from accounts.models import AccountBaseModel


class OrdersSyncService:
    """
    Service that synchronize orders between warehouses and stores.
    """
    ACCOUNT_AUTH_HEADER = 'Account-Authorization'

    def create_order(self, order: OrderBaseModel, serializer: Type[Serializer],
                     account: Type[AccountBaseModel]) -> Response:
        response = requests.post(account.path, data=serializer(order).data,
                                 headers={self.ACCOUNT_AUTH_HEADER: account.token})
        response.raise_for_status()
        return response

    def update_order(self, order: OrderBaseModel, serializer: Type[Serializer],
                     account: Type[AccountBaseModel]) -> Response:
        response = requests.patch(f'{account.path}/{order.number}', data=serializer(order).data,
                                  headers={self.ACCOUNT_AUTH_HEADER: account.token})
        response.raise_for_status()
        return response
