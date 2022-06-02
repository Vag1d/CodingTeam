from django.urls import path, include

from mainapp.views import FoodsView

as_view_common = {"get": "list", "post": "create"}

urlpatterns = [
    path('foods/', FoodsView.as_view(as_view_common), name='foods_list'),
]
