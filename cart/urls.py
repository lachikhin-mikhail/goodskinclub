from django.urls import path
from .views import cart, checkout, delivery, create, delete, deleteOne

urlpatterns = [
    path('', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('delivery', delivery, name='delivery'),
    path('create', create, name='create'),
    path('delete', delete, name='delete'),
    path('deleteOne', deleteOne, name='deleteOne'),

    ]
