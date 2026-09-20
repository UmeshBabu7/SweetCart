from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Category
from products.serializers import CategorySerializer


@api_view(["GET"])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
