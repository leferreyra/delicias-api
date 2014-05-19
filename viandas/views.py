from viandas.models import Dish, Offer, Order
from viandas.serializers import DishSerializer, OfferSerializer, OrderSerializer
from rest_framework import viewsets



class DishViewSet(viewsets.ModelViewSet):

	queryset = Dish.objects.all()
	serializer_class = DishSerializer



class OfferViewSet(viewsets.ModelViewSet):

	queryset = Offer.objects.all()
	serializer_class = OfferSerializer



class OrderViewSet(viewsets.ModelViewSet):

	queryset = Order.objects.all()
	serializer_class = OrderSerializer