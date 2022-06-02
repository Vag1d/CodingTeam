from django.test import TestCase

from mainapp.models import Food, FoodCategory


# Create your tests here.

class FoodTest(TestCase):
    def test_setUp(self):
        FoodCategory.objects.create(name_ru="Закуски")

        Food.objects.create(
            category_id=1,
            name_ru="Спрайт",
            code=100,
            internal_code=100,
            cost=123.50,
            is_publish=True,
        )

        Food.objects.create(
            category_id=1,
            name_ru="Пепси-Кола",
            code=100,
            internal_code=200,
            cost=123.50,
            is_publish=False,
        )

    def test_food_category(self):
        response = self.client.get("/api/v1/foods/")
        self.assertEqual(response.status_code, 200)