# from djongo import models
from django.db import models
import os
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
class FormData(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    tel = models.CharField(max_length=13)
    activated = models.BooleanField(default=False)
    token = models.CharField(max_length=100, blank=True, null=True)
    balance = models.IntegerField(default=500)
    path_avatar = models.TextField(default=f"{settings.STATIC_ROOT}media/profile.jpg")
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.fname} {self.lname}'


class Tickets(models.Model):
    client = models.ForeignKey(FormData, on_delete=models.CASCADE, related_name='tickets')
    barcode = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.id} - {self.barcode}'


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Bus(models.Model):
    name = models.CharField(max_length=100)
    frequency = models.IntegerField()
    depart_time = models.TimeField()
    end_time = models.TimeField()
    travel_time = models.IntegerField()
    number_of_buses = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='bus')

    def __str__(self):
        return f'{self.name}'


class Station(models.Model):
    station_id = models.IntegerField()
    order = models.IntegerField(default = 0)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='ord_stat')
    location = models.CharField(max_length=100)
    terminus = models.BooleanField()
    
    def __str__(self):
        return f'{self.station_id}'


@receiver(pre_delete, sender=FormData)
def formdata_pre_delete_handler(sender, instance, **kwargs):
    br_code = os.path.join(settings.STATIC_ROOT, "barcodes", f"{instance.email}.png")
    if os.path.exists(br_code):
        os.remove(br_code)
    avatar = instance.path_avatar
    if os.path.exists(avatar):
        os.remove(avatar)
    User.objects.get(username=instance.email).delete()
