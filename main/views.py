from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from main.models import Car, CarBrand
from main.serializers import CarBrandSerializer, CarBrandSingleSerializer, CarSerializer


class CarBrandListView(ListAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class BrandDetailView(RetrieveAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSingleSerializer


class CarDetailView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
