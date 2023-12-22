from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

ORDERED = 'ordered'
SHIPPED = 'shipped'
STATUS_CHOISES = (
    (ORDERED, 'Ordered'),
    (SHIPPED, 'Shipped')
)


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders',null=True , blank=True , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address =models.CharField(max_length=255)
    zipcode =models.CharField(max_length=255)
    place =models.CharField(max_length=255)
    phone =models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOISES, default=ORDERED)

    class Meta:
        ordering = ('-created_at',)

    def get_total_price(self):
        if self.paid_amount:
            return self.paid_amount /100
        return 0



class OrderedItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return self.price /100
    



    
