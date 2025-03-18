from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "is_active", "price", "get_orders_last_month", "get_orders_this_month")
    list_filter = ("category", "is_active")
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "order_date", "quantity")
    list_filter = ("order_date",)