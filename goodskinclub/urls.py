
from django.contrib import admin
from django.urls import path, include
from products.views import home
from skintest.views import skintest, result
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('favorites/', include('favorites.urls')),
    path('skintest/', skintest, name='skintest'),
    path('skintest/result', result, name='result'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
