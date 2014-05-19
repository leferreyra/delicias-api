from viandas.models import Dish, Offer, Order
from rest_framework import serializers



class DishSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:

		model = Dish



class OfferSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:

		model = Offer



class OrderSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:

		model = Order
