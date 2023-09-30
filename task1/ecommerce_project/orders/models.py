from django.db import models

class Order(models.Model):
    orderId = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    shipping_status = models.CharField(max_length=50)
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_payment_status = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderItems', on_delete=models.CASCADE)
    item_sid = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    tax_perc = models.IntegerField()
    tax_amt = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    tracking_number = models.CharField(max_length=50)
    canceled = models.CharField(max_length=1)
    shipped_status_sku = models.CharField(max_length=50)
    barcode = models.CharField(max_length=20, null=True, blank=True)
