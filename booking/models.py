from django.db import models
from room.models import Room
from django.utils import timezone

# Create your models here.


class Customer(models.Model):
    firstName = models.CharField(max_length=50, null= True)
    lastName = models.CharField(max_length=50)
    contactNum = models.IntegerField
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


class Booking(models.Model):
    roomID = models.ForeignKey(Room, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    saleID = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True, blank=True)
    bookingDate = models.DateField(auto_now_add=True)
    checkin = models.DateField(auto_now=False, editable=True, default='')
    checkout = models.DateField(auto_now=False, editable=True, default='')


class Payment(models.Model):
    bookingID = models.ForeignKey(Booking, on_delete=models.CASCADE)
    saleID = models.ForeignKey(Sale, on_delete=models.CASCADE)
    amount = models.IntegerField
    paymentType = models.CharField(max_length=50)
    paymentDate = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)


