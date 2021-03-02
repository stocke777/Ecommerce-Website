from django.contrib import admin
from .models import Product, Category, ProductImage
# Register your models here.

admin.site.register(Category)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [ ProductImageInline, ]

admin.site.register(Product, ProductAdmin)