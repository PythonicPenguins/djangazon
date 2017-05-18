from django.contrib import admin
from .models import Order, OrderProduct, PaymentType, Category

admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(PaymentType)
admin.site.register(Category)

