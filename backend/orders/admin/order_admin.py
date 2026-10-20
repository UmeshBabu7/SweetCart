from django.contrib import admin
from orders.models.order_models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "created_at", "total_amount"]
