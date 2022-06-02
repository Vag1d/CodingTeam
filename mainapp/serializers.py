from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from mainapp.models import Food, FoodCategory


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        model = Food
        fields = ('internal_code', 'code', 'name_ru', 'description_ru', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')


class FoodListSerializer(serializers.ModelSerializer):
    foods = SerializerMethodField()

    def get_foods(self, category):
        qs = Food.objects.filter(is_publish=True, category=category)
        serializer = FoodSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')

