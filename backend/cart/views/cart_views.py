from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.models import Cart
from cart.serializers import CartSerializer


@api_view(["GET"])
def get_cart(request):
    cart, created = Cart.objects.get_or_create(user=None)
    serializer = CartSerializer(cart)
    return Response(serializer.data)
