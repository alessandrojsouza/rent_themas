from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=60, blank=False)

    def __str__(self):
        return self.name

class Theme(models.Model):
    name = models.CharField(max_length=20, blank=False)
    color = models.CharField(max_length=10)
    price = models.FloatField()
    itens =  models.ManyToManyField('Item', related_name='themes')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=200)
    #theme = models.ForeignKey('Theme', on_delete=models.CASCADE, related_name='itens')

    def __str__(self):
        return self.name

class Rent(models.Model):
    date = models.DateField(blank=False, null=False)
    start_hours = models.CharField(max_length=5, blank=False, null=False)
    end_hours = models.CharField(max_length=5, blank=False, null=False)
    client = models.ForeignKey('Client', on_delete=CASCADE, related_name='rents')
    theme = models.ForeignKey('Theme', on_delete=CASCADE, related_name='rents')

    def __str__(self):
        return str(self.date)
    