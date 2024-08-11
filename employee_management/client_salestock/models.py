from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Client(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='pictures/')
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    remaining_balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))



    def __str__(self):
        return self.name

class StockSale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.IntegerField()
    payment_method = models.CharField(max_length=20)
    client_payed = models.DecimalField(max_digits=10, decimal_places=2)
    total_order_count = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    after_discount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
