from django.shortcuts import redirect, render
from .models import Client
# Create your views here.

#Página inicial com a lista de clientes
def index(request):
    clients_list = Client.objects.all()
    context = {'clients_list': clients_list}
    return render(request, 'index.html', context)

#Redirecionador para o formulário de cadastro
def formClient(request):
    return render(request, 'formClient.html')

#Salva o novo cliente e volta para listagem de clientes
def saveClient(request):
   c = Client(name=request.POST['name'])
   c.save()
   return redirect('/')

#Deleta um cliente e volta para listagem de clientes
def deleteClient(request, id):
    c = Client.objects.get(pk=id)
    c.delete()
    return redirect('/')

#Pega um cliente pelo ID e enviar para o form de edição
def detailClient(request, id):
   client = Client.objects.get(pk=id)
   return render(request, 'formEditClient.html', {'client': client} )

#Atualiza um cliente e volta para listagem
def updateClient(request, id):
    c = Client.objects.get(pk=id)
    c.name = request.POST['name']
    c.save()
    return redirect('/')