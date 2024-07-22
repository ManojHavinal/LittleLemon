from django.db import models
from django.utils import timezone

class Booking_table(models.Model):
    Name = models.CharField(max_length=225)
    no_of_guests = models.IntegerField(default=0)
    Booking_date = models.DateTimeField(default=timezone.now)  # Set default value here


class Menu_table(models.Model):
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    Inventory = models.IntegerField(default=0)              # Changed 'Inventory' to 'inventory' for consistency


