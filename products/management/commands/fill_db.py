from django.core.management.base import BaseCommand
from products.models import Product, Order
from django.utils.timezone import now
from random import randint, choice


class Command(BaseCommand):
    help = "Заполняет базу тестовыми данными"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Order.objects.all().delete()

        categories = ["Электроника", "Одежда", "Книги", "Игрушки"]
        for i in range(10):
            product = Product.objects.create(
                name=f"Товар {i+1}",
                category=choice(categories),
                is_active=choice([True, False]),
                price=randint(500, 5000),
            )

            for _ in range(randint(5, 15)):
                Order.objects.create(
                    product=product,
                    order_date=now().date().replace(day=randint(1, 28)),
                    quantity=randint(1, 5),
                )

        self.stdout.write(self.style.SUCCESS("База успешно заполнена тестовыми данными!"))
