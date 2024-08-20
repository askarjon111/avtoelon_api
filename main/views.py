from django_filters.rest_framework import DjangoFilterBackend
from django_filters.views import FilterView

from rest_framework.generics import ListAPIView, RetrieveAPIView

from main.filters import CarFilter
from main.models import Car, CarBrand
from main.serializers import CarBrandSerializer, CarBrandSingleSerializer, CarSerializer


class CarBrandListView(ListAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class BrandDetailView(RetrieveAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSingleSerializer


class CarsView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['brand', 'price', 'name', 'price__gte', 'price__lte']
    filterset_class = CarFilter


class CarDetailView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
