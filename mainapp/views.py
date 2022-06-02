from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from mainapp.models import FoodCategory
from mainapp.serializers import FoodListSerializer


class FoodsView(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.order_by('id')
    serializer_class = FoodListSerializer
    filter_backends = (OrderingFilter,)

