from rest_framework import serializers
from .models import MenuItem, Order, Delivery, Ingredient, Dish


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Dish
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    dish = DishSerializer()
    ingredients = IngredientSerializer(many=True, read_ony=True)

    class Meta:
        model = MenuItem
        fields = ['__all__']
