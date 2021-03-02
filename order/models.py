from django.db import models
from django.db.models.fields import CharField, DecimalField
from django.db.models.fields.related import ForeignKey
# Create your models here.

class Order(models.Model):
    user = ForeignKey("users.User", on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(default="PENDING", max_length=10)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.email

class OrderItem(models.Model):
    order = ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item.name