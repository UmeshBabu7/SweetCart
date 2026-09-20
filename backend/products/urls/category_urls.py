from django.urls import path
from products.views.category_views import get_categories

urlpatterns = [
  path('categories/', get_categories),
]