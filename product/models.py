from django.db import models
from django.core.validators import MaxLengthValidator

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(validators=[MaxLengthValidator(2000)])
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    mrp = models.IntegerField()
    price = models.IntegerField()
    brand = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.name

    def available(self):
        return self.quantity>0


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'product_images')