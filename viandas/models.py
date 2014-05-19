from django.db import models
from django.contrib.auth.models import User


class Dish(models.Model):

	name = models.CharField(max_length=100)
	ingredients = models.CharField(max_length=100)

	def __unicode__(self):

		return self.name

	class Meta:

		verbose_name_plural = "Dishes"


class Offer(models.Model):

	dish = models.ForeignKey(Dish)
	date = models.DateField()
	price = models.DecimalField(decimal_places=2, max_digits=4)

	def __unicode__(self):

		return "%s %s" % (self.dish, self.date)


class Order(models.Model):

	offer = models.ForeignKey(Offer)
	user = models.ForeignKey(User)


