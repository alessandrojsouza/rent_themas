from dataclasses import fields
from rent.models import Client, Item, Phone, Rent, Theme
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
   phones = serializers.SerializerMethodField()
         
   def get_phones(self, obj):
       return obj.phones.values()
   class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phones']
        #fields ='__all__'
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
        
class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'