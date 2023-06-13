from django.contrib import admin

from Restaurant.models import Ingredient, Dish, MenuItem, Order, OrderItem, Delivery

admin.site.register(Ingredient)
admin.site.register(Dish)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Delivery)
