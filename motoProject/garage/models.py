import datetime

from django.db import models
from django.utils import timezone


class Motorcycle(models.Model):
    motorcycle_text = models.CharField(max_length=200)
    
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.motorcycle_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Description(models.Model):
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)
    description_text = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.description_text