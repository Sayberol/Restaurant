from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from .models import Delivery
from .serializers import DeliverySerializer


class DeliveryListCreateView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'driver']
    search_fields = ['status', 'driver']
    ordering_fields = ['status', 'driver']
