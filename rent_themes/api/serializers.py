from pyexpat import model
from rent.models import Client, Item, Rent, Theme
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email']

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'