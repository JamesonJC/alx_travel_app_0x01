from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    # assume you already have this model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # ... other fields ...

class Payment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Booking {self.booking.id} - {self.status}"

