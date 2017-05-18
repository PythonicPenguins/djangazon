"""Models for the Bangazon application."""
from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Product(models.Model):
    """Products within the Bangazon application are represented by this model.

    Author: Steve Brownlee
    Args: Extends the models.Model Django class
    Return: N/A
    """

    seller = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()


class PaymentType(models.Model):
    """PaymentTypes within the Bangazon application are represented by this model.

    Author: Meg Ducharme
    Args: Extends the models.Model Django class
    Return: N/A
    """

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )
    name = models.CharField(max_length=55)
    account_number = models.CharField(max_length=16)


class Order(models.Model):
    """Order within the Bangazon application are represented by this model.

    Author: Meg Ducharme
    Args: Extends the models.Model Django class
    Return: N/A
    """

    customer = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )
    payment_type = models.ForeignKey(
        PaymentType,
        on_delete=models.DO_NOTHING,
    )
    date_created = date.today()


class OrderProduct(models.Model):
    """OrderProduct within the Bangazon application are represented by this model.

    Author: Meg Ducharme
    Args: Extends the models.Model Django class
    Return: N/A
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.DO_NOTHING,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
    )


class Category(models.Model):
    """Categories within the Bangazon application are represented by this model.

    Author: Gilberto Diaz
    Args: Extends the models.Model Django class
    Return: N/A
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        """Appliying __str__ to the name feature of the Category model.

        Author: Gilberto Diaz
        Args: Extends the models.Model Django class
        Return: A readeble representation of the object
        """
        return self.name

