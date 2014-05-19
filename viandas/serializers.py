from viandas.models import Dish, Offer, Order
from django.contrib.auth.models import User
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:

		model = User
		fields = ('id', 'username', 'email', 'first_name', 'last_name')



class DishSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:

		model = Dish



class OfferSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:

		model = Offer



class OrderSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:

		model = Order
