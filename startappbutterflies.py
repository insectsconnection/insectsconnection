#python manage.py startapp butterflies
from tkinter import CASCADE
from turtle import ondrag
import django.db.models.deletion
from datetime import datetime
from django.utils import timezone
from django.forms import DateTimeField
from django.db import models
from django.contrib.auth.models import AbstractUser


class Lepidoptera(models.Model):
    scientific_subspecies_name = models.CharField(max_length=30)
    local_name = models.CharField(max_length=30)
    english_name = models.CharField(max_length=30)
    discovered_by = models.CharField(max_length=30)
    year_field = DateTimeField(datetime.now, blank=True)
    family = models. CharField(max_length=30)
    location = models.CharField(max_length=30)
    date = models.DateField(_("Date"), auto_now_add=True)
    date = models.DateField(default=datetime.date.today, blank=True, null=True)
    date_added = models.DateTimeField(
    default=timezone.localtime, blank=True, null=True)
    text = models.TextField()




def __str__(self):
    return self.id + " " + self.scientific_subspecies_name




class EventPhoto(models.Model):
    event_id = models.ForeignKey(Lepidoptera, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='news/')
