from django.contrib import admin

from .models import *

admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
"""Access from admin/superkey""