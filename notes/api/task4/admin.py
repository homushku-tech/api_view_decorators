from django.contrib import admin
from api.task4.models import Product, Order, OrderItem

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)