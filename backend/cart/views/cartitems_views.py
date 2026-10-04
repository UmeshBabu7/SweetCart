from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from cart.models import CartItem, Cart
from cart.serializers import CartSerializer


@api_view(["POST"])
def add_to_cart(request):
    product_id = request.data.get("product_id")
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=None)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        item.quantity += 1
        item.save()

    return Response(
        {"message": "Product added to cart", "cart": CartSerializer(cart).data}
    )


@api_view(["POST"])
def remove_from_cart(request):
    item_id = request.data.get("item_id")
    CartItem.objects.filter(id=item_id).delete()
    return Response({"message": "Item removed from cart"})
