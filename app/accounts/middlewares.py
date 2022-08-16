from django.apps import apps
from django.conf import settings


class AccountAuthMiddleware:
    """
    Adds 'account' to request if 'Account-Authorization' in request headers
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        app_name, model_name = settings.ACCOUNT_MODEL.split('.')
        account_model = apps.get_model(app_name, model_name)

        token = request.headers.get('Account-Authorization')

        if token:
            account = account_model.objects.filter(token=token).first()
            if account:
                request.account = account
        return self.get_response(request)
