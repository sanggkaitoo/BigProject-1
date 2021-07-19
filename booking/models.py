from django.db import models
from AnKhangHotel import settings
from room.models import Room
from django.utils import timezone

# Create your models here.


class Customer(models.Model):
    firstName = models.CharField(max_length=50, null= True)
    lastName = models.CharField(max_length=50)
    contactNum = models.CharField(max_length=10, default='0123456789')
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=10, choices=gender)
    idProof = models.CharField(max_length=20)
    contactMail = models.EmailField(default='')

    def __str__(self):
        return '{} {}'.format(self.firstName, self.lastName)


class Sale(models.Model):
    saleTitle = models.CharField(max_length=100)
    salePercent = models.IntegerField
    startDate = models.DateField
    endDate = models.DateField
    repeat = models.CharField(max_length=10)
    description = models.TextField(default='')
    status = models.BooleanField(default=True)


class Payment(models.Model):
    saleID = models.ForeignKey(Sale, on_delete=models.CASCADE, null= True, blank=True)
    amount = models.IntegerField()
    paymentTypeChoices = (
        ('Momo', 'Momo'),
        ('Visa/Debit/Mastercard', 'Visa/Debit/Mastercard'),
        ('Paypal', 'Paypal')
    )
    paymentType = models.CharField(max_length=50, choices=paymentTypeChoices)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE, default='')
    paymentDate = models.DateTimeField(auto_now=True)
    checkin = models.DateField(auto_now=False, editable=True, default='')
    checkout = models.DateField(auto_now=False, editable=True, default='')
    note = models.TextField(default='')
    status = models.BooleanField(default=False)


class Booking(models.Model):
    paymentID = models.ForeignKey(Payment, on_delete=models.CASCADE, default='')
    roomID = models.ForeignKey(Room, on_delete=models.CASCADE)
    bookingDate = models.DateField(auto_now_add=True)
    checkin = models.DateField(auto_now=False, editable=True, default='')
    checkout = models.DateField(auto_now=False, editable=True, default='')
    children = models.IntegerField(default=1)
    adults = models.IntegerField(default=0)


