from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

from api.serializers import *
from rent.models import *

# Create your views here.

class ClientViewSet(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
       client = Client(name=request.data['name'],
                       email=request.data['email']) 
       serializer = ClientSerializer(client)
       serializer.save()
       if(request.data['ddd1']!=''):
                t1 = Phone(ddd=request.data['ddd1'],
                        number=request.data['phone1'],
                        client=client)
                serializer =PhoneSerializer(t1)
                serializer.save()
        
       if(request.data['ddd2']!=''):
                    t2 = Phone(ddd=request.data['ddd2'],
                        number=request.data['phone2'],
                        client=client)
                    serializer =PhoneSerializer(t2)
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer

class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
class PhoneByClient_IdViewSet(viewsets.ModelViewSet):
    pass

class AddressByRent_IdViewSet(viewsets.ModelViewSet):
    pass