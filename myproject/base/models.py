from django.db import models

# Create your models here.

class Flights(models.Model):
    flight_name = models.CharField(max_length=20)
    flight_source = models.CharField(max_length=30)
    flight_dest = models.CharField(max_length=30)
    flight_timming = models.FloatField()
    ticket_price = models.FloatField()
    date = models.CharField(max_length=10)

class user_tickets(models.Model):
    flight_name = models.CharField(max_length=20)
    flight_source = models.CharField(max_length=30)
    flight_dest = models.CharField(max_length=30)
    flight_timming = models.FloatField()
    ticket_price = models.FloatField()
    date = models.CharField(max_length=20)
    
    user_name = models.CharField(max_length=20)
    user_age = models.IntegerField()
    user_phone = models.IntegerField()
    user_email = models.EmailField()
    seat_class = models.CharField(max_length=10)
    seat_number = models.CharField(max_length=10)