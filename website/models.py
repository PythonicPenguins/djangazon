"""Models for the Bangazon application."""
from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    """Products within the Bangazon application are represented by this model.

    Author: Steve Brownlee
    Args: Extends the models.Model Django class
    Return: N/A
    """

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()


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
