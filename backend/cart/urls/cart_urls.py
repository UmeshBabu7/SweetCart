from django.urls import path
from cart.views.cart_views import get_cart
from cart.views.cartitems_views import add_to_cart, remove_from_cart, update_cart_quantity

urlpatterns = [
    path("cart/", get_cart),
    path("cart/add/", add_to_cart),
    path("cart/remove/", remove_from_cart),
    path('cart/update/', update_cart_quantity),
]
