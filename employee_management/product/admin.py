from django.contrib import admin
from .models import Category, Jacket, Pant, Shirt, Shorts, T_shirt, Trouser

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Jacket)
class JacketAdmin(admin.ModelAdmin):
    list_display = ('fabric_type', 'manafacturing_price', 'quantity', 'size', 'color', 'sale_price', 'total_price')
    list_filter = ('fabric_type', 'size', 'color')
    search_fields = ('fabric_type__name', 'size')

@admin.register(Pant)
class PantAdmin(admin.ModelAdmin):
    list_display = ('cutt_no', 'wash', 'quantity', 'piece_style', 'brand_name', 'color', 'manufacturing_price', 'sale_price', 'size', 'fabric_type', 'total_price')
    list_filter = ('fabric_type', 'size', 'color')
    search_fields = ('cutt_no', 'brand_name')

@admin.register(Shirt)
class ShirtAdmin(admin.ModelAdmin):
    list_display = ('fabric_type', 'manafacturing_price', 'quantity', 'size', 'color', 'sale_price', 'total_price')
    list_filter = ('fabric_type', 'size', 'color')
    search_fields = ('fabric_type__name', 'size')

@admin.register(Shorts)
class ShortsAdmin(admin.ModelAdmin):
    list_display = ('cutt_no', 'wash', 'quantity', 'piece_style', 'brand_name', 'color', 'manufacturing_price', 'sale_price', 'size', 'fabric_type', 'total_price')
    list_filter = ('fabric_type', 'size', 'color')
    search_fields = ('cutt_no', 'brand_name')

@admin.register(T_shirt)
class T_shirtAdmin(admin.ModelAdmin):
    list_display = ('fabric_type', 'manafacturing_price', 'quantity', 'size', 'color', 'sale_price', 'total_price')
    list_filter = ('fabric_type', 'size', 'color')
    search_fields = ('fabric_type__name', 'size')

@admin.register(Trouser)
class TrouserAdmin(admin.ModelAdmin):
    list_display = ('cutt_no', 'wash', 'quantity', 'piece_style', 'brand_name', 'color', 'manufacturing_price', 'sale_price', 'size', 'fabric_type', 'total_price')
    list_filter = ('fabric_type', 'size', 'color')
    search_fields = ('cutt_no', 'brand_name')
