from django.shortcuts import redirect, render
from .models import *


#Página inicial com a lista de clientes
def index(request):
    clients_list = Client.objects.all()
    context = {'clients_list': clients_list}
    return render(request, 'index.html', context)

### ### ### ### ### ## VIEWS PARA CDU CLIENTE ## ### ### ### ### ###
class ClientViews:

    def listClient(request):
        clients_list = Client.objects.all()
        context = {'clients_list': clients_list}
        return render(request, 'client/listClient.html', context)

    #Redirecionador para o formulário de cadastro
    def formClient(request):
        return render(request, 'client/formClient.html')

    #Salva o novo cliente e volta para listagem de clientes
    def saveClient(request):
        c = Client(name=request.POST['name'])
        c.save()
        return redirect('/listClient')

    #Deleta um cliente e volta para listagem de clientes
    def deleteClient(request, id):
        c = Client.objects.get(pk=id)
        c.delete()
        return redirect('/listClient')

    #Pega um cliente pelo ID e enviar para o form de edição
    def detailClient(request, id):
        client = Client.objects.get(pk=id)
        return render(request, 'client/formEditClient.html', {'client': client} )

    #Atualiza um cliente e volta para listagem
    def updateClient(request, id):
        c = Client.objects.get(pk=id)
        c.name = request.POST['name']
        c.save()
        return redirect('/listClient')

### ### ### ### ### ## VIEWS PARA CDU TEMAS ## ### ### ### ### ###
class ThemeViews:
    #Recupera a lista de temas cadastrados
    def listTheme(request):
        themes_list = Theme.objects.all()
        context = {'theme_list': themes_list}
        return render(request, 'theme/listTheme.html', context)

    #Redirecionador para o formulário de cadastro de temas com itens existentes
    def formTheme(request):
        list_item = Item.objects.all()
        return render(request, 'theme/formTheme.html', {'list_item':list_item})

    #Salva o novo tema e volta para listagem de temas
    def saveTheme(request):
        t = Theme(name=request.POST['name'], 
                    color=request.POST['color'], 
                    price=request.POST['price'],
                    )
        t.save()
        my_list = request.POST.getlist('item')

        for i in my_list:
            item = Item.objects.get(id=i)
            t.itens.add(item)
        t.save()
        return redirect('/listTheme')
    
    #Deleta um tema e volta para listagem de temas
    def deleteTheme(request, id):
        t = Theme.objects.get(pk=id)
        t.delete()
        return redirect('/listTheme')

    #Pega um tema pelo ID e enviar para o form de edição
    def detailTheme(request, id):
        theme = Theme.objects.get(pk=id)
        return render(request, 'theme/formEditTheme.html', {'theme': theme} )

    #Atualiza um tema e volta para listagem
    def updateTheme(request, id):
        t = Theme.objects.get(pk=id)
        t.name = request.POST['name']
        t.color = request.POST['color']
        t.price = request.POST['price']
        t.save()
        return redirect('/listTheme')

### ### ### ### ### ## VIEWS PARA CDU ITEM ## ### ### ### ### ###
class ItemViews:
    #Recupera a lista de itens cadastrados
    def listItem(request):
        item_list = Item.objects.all()
        context = {'item_list': item_list}
        return render(request, 'item/listItem.html', context)

    #Redirecionador para o formulário de cadastro de item
    def formItem(request):
        return render(request, 'item/formItem.html')

    #Salva o novo item e volta para listagem de itens
    def saveItem(request):
        i = Item(name=request.POST['name'], 
                 description=request.POST['description'])
        i.save()
        return redirect('/listItem')

    #Deleta um item e volta para listagem de itens
    def deleteItem(request, id):
        i = Item.objects.get(pk=id)
        i.delete()
        return redirect('/listItem')
    
    #Pega um item pelo ID e enviar para o form de edição
    def detailItem(request, id):
        item = Item.objects.get(pk=id)
        return render(request, 'item/formEditItem.html', {'item': item} )

    #Atualiza um item e volta para listagem
    def updateItem(request, id):
        i = Item.objects.get(pk=id)
        i.name = request.POST['name']
        i.description = request.POST['description']
        i.save()
        return redirect('/listItem')

### ### ### ### ### ## VIEWS PARA CDU ALUGUEIS ## ### ### ### ### ###
class RentViews:
    
    #Recupera a lista de aluguéis cadastrados
    def listRent(request):
        rent_list = Rent.objects.all()
        context = {'rent_list': rent_list}
        return render(request, 'rent/listRent.html', context) 
    
    #Redirecionador para o formulário de cadastro de aluguel
    def formRent(request):
        client_list = Client.objects.all()
        theme_list = Theme.objects.all()
        context = {'client_list':client_list, 'theme_list': theme_list}
        return render(request, 'rent/formRent.html', context)
    
    #Salva o novo aluguel e volta para listagem de alugueis
    def saveRent(request):
        r = Rent(date=request.POST['date'], 
                 start_hours=request.POST['start_hours'],
                 end_hours=request.POST['end_hours'],
                 client_id= request.POST['select_client'],
                 theme_id = request.POST['select_theme'])
        r.save()
        return redirect('/listRent')

    #Deleta um aluguel e volta para listagem de alugueis
    def deleteRent(request, id):
        i = Rent.objects.get(pk=id)
        i.delete()
        return redirect('/listRent')
    
    #Pega um aluguel pelo ID e enviar para o form de edição
    def detailRent(request, id):
        rent = Rent.objects.get(pk=id)
        return render(request, 'rent/formEditRent.html', {'rent': rent})
    
    #Atualiza um item e volta para listagem
    def updateRent(request, id):
        i = Rent.objects.get(pk=id)
        i.date = request.POST['date']
        i.start_hours=request.POST['start_hours']
        print(request.POST['end_hours'])
        i.end_hours=request.POST['end_hours']
        i.save()
        return redirect('/listRent')