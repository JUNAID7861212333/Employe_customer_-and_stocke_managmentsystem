from django.contrib import admin
from .models import Client, StockSale

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'whatsapp', 'gender', 'phone_number', 'remaining_balance')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('gender',)

@admin.register(StockSale)
class StockSaleAdmin(admin.ModelAdmin):
    list_display = ('client', 'product_name', 'product_price', 'product_quantity',
                    'payment_method', 'client_payed', 'total_order_count',
                    'discount_percentage', 'after_discount')
    list_filter = ('client', 'payment_method')
    search_fields = ('client__name', 'product_name')

