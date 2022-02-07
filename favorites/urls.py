from django.urls import path
from .views import favorites, toggleFav

urlpatterns = [
    path('', favorites, name='favorite'),
    path('toggleFav', toggleFav, name='toggleFav'),
    ]
