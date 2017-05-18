from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Product(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()


class PaymentType(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.DO_NOTHING,
    )
    name = models.CharField(max_length=55)
    account_number = models.CharField(max_length=16)


class Order(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete = models.DO_NOTHING,
    )
    payment_type = models.ForeignKey(
        PaymentType,
        on_delete = models.DO_NOTHING,
    )
    date_created = date.today()


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete = models.DO_NOTHING,
    )
    product = models.ForeignKey(
        Product,
        on_delete = models.DO_NOTHING,
    )
