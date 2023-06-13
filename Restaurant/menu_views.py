from django_filters.rest_framework import DjangoFilterBackend, RangeFilter
from rest_framework import generics, permissions, filters

from Restaurant.models import MenuItem, Dish, Ingredient
from Restaurant.serializer import MenuItemSerializer, DishSerializer, IngredientSerializer


class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['menu_name', 'name', 'price']
    search_fields = ['menu_name', 'name', 'price']
    ordering_fields = ['menu_name', 'name', 'price']


class MenuItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class DishListCreateView(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, RangeFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price']
    ordering = ['name']
    #Определите поле ценового диапазона для фильтрации
    filterset_fields = {
        'price': ['range']
    }


class DishRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticated]


class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['name', 'description']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'description']


class IngredientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]
