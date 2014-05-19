from viandas.models import Dish, Offer, Order
from django.contrib.auth.models import User
from viandas.serializers import DishSerializer, OfferSerializer, OrderSerializer, UserSerializer
from rest_framework import viewsets



class UserViewSet(viewsets.ModelViewSet):

	queryset = User.objects.all()
	serializer_class = UserSerializer



class DishViewSet(viewsets.ModelViewSet):

	queryset = Dish.objects.all()
	serializer_class = DishSerializer



class OfferViewSet(viewsets.ModelViewSet):

	queryset = Offer.objects.all()
	serializer_class = OfferSerializer



class OrderViewSet(viewsets.ModelViewSet):

	queryset = Order.objects.all()
	serializer_class = OrderSerializer