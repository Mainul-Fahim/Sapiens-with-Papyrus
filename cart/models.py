from django.contrib.auth.models import User
from django.db import models
from products.models import  ListView, DetailView
""" Imported from books featire"""


class orderitems(models.Model):
    customer = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    """If the book is available on database then it will true"""

    def __str__(self):
        return str(self.id)
        
    @property
    def shipping(self):
        """get the order items"""
        orderitems = self.orderitem_set.all()
        
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 


    @property
    def get_total(self):
        total = self.Book.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Book on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address