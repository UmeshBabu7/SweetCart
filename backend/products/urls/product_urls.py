from django.urls import path
from products.views.product_views import get_products

urlpatterns = [
  path('products/', get_products),
]