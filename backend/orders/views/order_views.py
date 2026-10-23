from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from cart.models.cart_models import Cart
from orders.models.order_models import Order
from orders.models.orderitems_models import OrderItem


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_order(request):
    data = request.data

    name = data.get("name", "").strip()
    address = data.get("address", "").strip()
    phone = str(data.get("phone", "")).strip()
    payment_method = data.get("payment_method", "COD")

    # Validate name and address
    if not name or not address:
        return Response(
            {"error": "Name and address are required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Validate phone number
    if not phone.isdigit() or len(phone) != 10:
        return Response(
            {"error": "Enter a valid 10-digit phone number"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Validate payment method
    if payment_method not in ["COD", "ONLINE"]:
        return Response(
            {"error": "Invalid payment method"}, status=status.HTTP_400_BAD_REQUEST
        )

    # Get logged-in user's cart
    cart = Cart.objects.filter(user=request.user).first()

    if not cart:
        return Response({"error": "Cart not found"}, status=status.HTTP_400_BAD_REQUEST)

    items = list(cart.items.select_related("product").all())

    if not items:
        return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

    # Calculate total amount
    total = sum(item.product.price * item.quantity for item in items)

    # Create order and items
    order = Order.objects.create(user=request.user, total_amount=total)

    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )

    # Clear cart after order creation
    cart.items.all().delete()

    return Response(
        {"message": "Order created successfully", "order_id": order.id, "total": total},
        status=status.HTTP_201_CREATED,
    )
