import datetime

from django.db import models
from django.utils import timezone


class Motorcycle(models.Model):
    motorcycle_text = models.CharField(max_length=200)
    motorcycle_brand = models.CharField(max_length=20, default="No brand")
    motorcycle_description = models.CharField(max_length=500, default="No description")
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.motorcycle_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
