from django.contrib import admin
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ( 'product',  'get_variations', 'cart', 'quantity', 'is_active')

    def get_variations(self, obj):
        return ", ".join([str(variation) for variation in obj.variations.all()])
    get_variations.short_description = 'Variations'

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)

# Register your models here.
