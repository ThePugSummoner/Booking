from django.db import models
from datetime import datetime

# Menu model
class Menu(models.Model):
    item_name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1000)

    def __str__(self) -> str:
        return self.item_name
    
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self) -> str:
        return self.first_name