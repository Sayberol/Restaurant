from django.urls import path

from Restaurant import views

urlpatterns = [
    path('api/menus/', views.api_menu),
    path('api/menus/<int:pk>/', views.api_menu_item_detail),
    path('api/orders/', views.order_list),
    path('api/orders/<int:pk>/', views.order_detail),
    path('api/deliveries/', views.delivery_list),
    path('api/deliveries/<int:pk>/', views.delivery_detail),
    path('api/deliveries/create/', views.delivery_create),
]
