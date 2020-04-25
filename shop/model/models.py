from django.db import models
from django.contrib.auth.models import User

from shop.model import brands


class Profile(models.Model):
    """Check AbstractUser class in django.contrib.auth.models for other fields"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, blank=True)
    address = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    telephone_number = models.CharField(max_length=14, blank=True)      # +989998887766 -> 13
    # order_history = models.   # an array of orders


class Entity(models.Model):
    entity_name = models.CharField(max_length=200)
    entity_price = models.FloatField(blank=True)
    discount_percent = models.DecimalField()    # Always below 1.0
    model = models.CharField(max_length=30, blank=True, null=True, choices=brands.Brands.choices())

    def __str__(self):
        return '{}, price:{}'.format(self.entity_name, self.entity_price)


class Order(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False)  # Don't make auto_now=True
    owner = models.OneToOneField(Profile)
    entities = models.ManyToManyField(Entity)   # This should be one to many
    is_finalized = models.BooleanField(default=False)   # If true the price is paid
    is_complete = models.BooleanField(default=False)    # Is delivered to post community or costumer

    def price_amount(self):
        sum_of_prices = 0.0
        for entity in self.entities.all():
            sum_of_prices += entity.entity_price * (1.0 - entity.discount_percent)
        return sum_of_prices
