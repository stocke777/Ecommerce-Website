from django.contrib import admin
from .models import Cart, Item

# Register your models here.
# admin.site.register(Cart)

class ItemInline(admin.TabularInline):
    model = Item

class CartAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]
admin.site.register(Cart, CartAdmin)