from django.db import models
from django.utils.timezone import now
from datetime import timedelta


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    category = models.CharField(max_length=100, verbose_name="Категория")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def get_orders_last_month(self):
        today = now().date()
        first_day_last_month = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
        last_day_last_month = today.replace(day=1) - timedelta(days=1)

        return self.orders.filter(order_date__range=(first_day_last_month, last_day_last_month)).count()

    def get_orders_this_month(self):
        today = now().date()
        first_day_this_month = today.replace(day=1)

        return self.orders.filter(order_date__gte=first_day_this_month).count()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="orders", verbose_name="Товар"
    )
    order_date = models.DateField(verbose_name="Дата заказа")
    quantity = models.PositiveIntegerField(verbose_name="Количество")

    def __str__(self):
        return f"Заказ {self.id} - {self.product.name}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"