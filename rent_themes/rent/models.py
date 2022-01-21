from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=60, blank=False)
    email = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return self.name

class Phone(models.Model):
    ddd = models.CharField(max_length=3)
    number = models.CharField(max_length=10)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='phones')
    
    def __str__(self):
        return self.client.name+ ' ' + self.number
    
    
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
    address = models.OneToOneField('Address', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.date) + ' ' + self.client.name + ' ' + self.theme.name
    
class Address(models.Model):
    street = models.CharField(max_length=60)
    number = models.IntegerField(null=True)
    complement = models.CharField(max_length=50)
    district = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.street
    