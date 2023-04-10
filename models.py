from enum import unique
import imp
from operator import mod
from platform import java_ver
from pyexpat import model
from statistics import mode
from sys import flags
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User, AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
import uuid

class Signup(models.Model):
    firstName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.firstName


# class User(AbstractUser):
#     is_admin=models.BooleanField(default=False)
#     is_customer=models.BooleanField(default=False)

   

# class adminUser(models.Model):
#     hotelName = models.CharField(max_length=50, null=False, blank=False)
#     location = models.CharField(max_length=50, null=False, blank=False)
#     city = models.CharField(max_length=50, null=False, blank=False)
#     state = models.CharField(max_length=50, null=False, blank=False)
#     zipcode = models.IntegerField( null=False, blank=False)
   
# class customeruser(models.Model):
#     firstName = models.CharField(max_length=50, null=False, blank=False)
#     lastName = models.CharField(max_length=50, null=False, blank=False)
#     email = models.EmailField(max_length=50, null=False, blank=False)
  


class profile(models.Model):
    def namefile(instance, filename):
        return  '/'.join(['images',str(instance.name),filename])
    name=models.CharField(max_length=200)
    picture=models.ImageField(upload_to=namefile, blank=True)
    def __str__(self):
        return  self.name


class Hotels(models.Model):
    hotelID=models.AutoField(primary_key=True,editable=False)
    hotelName=models.CharField(max_length=60, null=False, blank=False)
    zipCode=models.IntegerField( null=False, blank=False)
    city=models.CharField(max_length=30, null=False, blank=False)
    state = models.CharField(max_length=30, null=False, blank=False)
    hotel_location = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.hotelName


class Rooms_info(models.Model):
    def namefile(instance, filename):
        return '/'.join(['images', str(instance.room_number), filename])
    room_number =models.AutoField(primary_key=True,editable=False)
    room_type = models.CharField(max_length=60, null=False, blank=False)
    room_price = models.FloatField(max_length=200, null=False, blank=False)
    number_of_beds = models.IntegerField( null=False, blank=False)
    hotelID=models.ForeignKey(Hotels,null=True,on_delete=models.CASCADE)
    roomImage=models.ImageField(upload_to=namefile, blank=True)


class User(models.Model):
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

class customer_details(models.Model):
    id =models.AutoField(primary_key=True,editable=False)
    PhoneNumber=models.CharField(max_length=60, null=False, blank=False)
    firstName=models.CharField(max_length=60, null=False, blank=False)
    lastName=models.CharField(max_length=60, null=False, blank=False)
    city=models.CharField(max_length=30, null=False, blank=False)
    state = models.CharField(max_length=30, null=False, blank=False)
    
    def __str__(self):
        return self.firstName

class customer_info(models.Model):
    
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    customerId=models.AutoField(primary_key=True,editable=False)
    id=models.ForeignKey(customer_details,null=True,on_delete=models.CASCADE)

   

class Reservation(models.Model):

    reservationNumber=models.AutoField(primary_key=True,editable=False)
    CustomerId=models.ForeignKey(customer_info,null=True,on_delete=models.CASCADE)
    checkInDateTime=models.DateField( null=False, blank=False)
    checkOutDateTime=models.DateField( null=False, blank=False)
    reservationGuest = models.CharField(max_length=30, null=False, blank=False)
    numberOfGuest=models.IntegerField( null=False, blank=False)
    def __str__(self):
        return self.reservationGuest

class customer(models.Model):
    class Meta:
        unique_together=(('customerId', 'reservationNumber'),)
    customerId=models.ForeignKey(customer_info,null=True,on_delete=models.CASCADE)
    reservationNumber=models.ForeignKey(Reservation,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.customerId


class billingInfo(models.Model):
    class Meta:
        unique_together=(('billingId','reservationNumber'),)

    billingId=models.AutoField(primary_key=True,editable=False)
    reservationNumber=models.ForeignKey(Reservation,null=True,on_delete=models.CASCADE)
    totalBilling = models.FloatField(null=False, blank=False)
    paymentDate = models.DateField( null=False, blank=False)
    

    def __str__(self):
        return self.billingId



class services(models.Model):
    serviceId=models.AutoField(primary_key=True, editable=False)
    serviceName = models.CharField(max_length=30, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.serviceName

class service_info(models.Model):
    class Meta:
        unique_together=(('serviceId','hotelId','reservationNumber'),)

    serviceId=models.ForeignKey(services,null=True,on_delete=models.CASCADE)
    hotelId=models.ForeignKey(Hotels,null=True,on_delete=models.CASCADE)
    reservationNumber=models.ForeignKey(Reservation,null=True,on_delete=models.CASCADE)
    qunatity=models.IntegerField(null=False, editable=False)
    totalServicePrice = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.totalServicePrice
class rooms(models.Model):
    class Meta:
        unique_together=(('roomNumber','hotelId','reservationNumber'),)

    roomNumber=models.ForeignKey(Rooms_info,null=True,on_delete=models.CASCADE)
    hotelId=models.ForeignKey(Hotels,null=True,on_delete=models.CASCADE)
    reservationNumber=models.ForeignKey(Reservation,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.roomNumber
