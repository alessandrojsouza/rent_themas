from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Theme(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    price = models.FloatField()
    itens =  models.ManyToManyField('Item', related_name='themes')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
   # theme = models.ForeignKey('Theme', on_delete=models.CASCADE, related_name='itens', default='0')

    def __str__(self):
        return self.name