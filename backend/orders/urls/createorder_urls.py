from django.urls import path
from orders.views.order_views import create_order

urlpatterns = [
    path('orders/create/', create_order),
]