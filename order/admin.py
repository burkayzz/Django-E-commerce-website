from django.contrib import admin
from .models import Cart,CartItem,Order,OrderItem,Shipment
# Register your models here.


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ["user"]
    class Meta:
        model = Cart

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = ["product"]

    class Meta:
        model = CartItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    class Meta:
        model = Order

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    
    class Meta:
        model = OrderItem

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):

    search_fields=["order"]
    list_display = ["order","user","created_at"]  
    


    class Meta:
        model = Shipment

    