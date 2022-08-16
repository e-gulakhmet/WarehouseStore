from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
]

# Web API
if 'store' in settings.INSTALLED_APPS:
    urlpatterns.append(path('store/', include('store.urls', namespace='store')))
if 'warehouse' in settings.INSTALLED_APPS:
    urlpatterns.append(path('warehouse/', include('warehouse.urls', namespace='warehouse')))
