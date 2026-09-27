from django.urls import path
from products.views.product_views import get_products, get_product

urlpatterns = [path("products/", get_products), path("products/<int:id>/", get_product)]
