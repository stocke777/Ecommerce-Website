from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    class Meta:
        model = Order
        
admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem)

