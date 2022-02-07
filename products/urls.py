from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>', views.detail, name='detail'),
    path('', views.products, name='products'),
    path('<path:category>/<path:skinType>', views.products),
    path('<path:category>', views.products),



]
