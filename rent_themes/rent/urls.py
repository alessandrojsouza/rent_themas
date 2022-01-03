from django.urls import path

from .views import index, ClientViews, ThemeViews, ItemViews, RentViews

urlpatterns= [

    #URLs para página principal
    path('', index),

    #URLs para CDUs Cliente
    path('listClient/', ClientViews.listClient),
    path('formClient/', ClientViews.formClient),
    path('saveClient/', ClientViews.saveClient),
    path('deleteClient/<int:id>', ClientViews.deleteClient),
    path('detailClient/<int:id>', ClientViews.detailClient),
    path('updateClient/<int:id>', ClientViews.updateClient),

    #URLs para CDUs Itens
    path('listItem/', ItemViews.listItem),
    path('formItem/', ItemViews.formItem),
    path('saveItem/', ItemViews.saveItem),
    path('deleteItem/<int:id>', ItemViews.deleteItem),
    path('detailItem/<int:id>', ItemViews.detailItem),
    path('updateItem/<int:id>', ItemViews.updateItem),

    #URLs para CDUs Temas
    path('listTheme/', ThemeViews.listTheme),
    path('formTheme/', ThemeViews.formTheme),
    path('saveTheme/', ThemeViews.saveTheme),
    path('deleteTheme/<int:id>', ThemeViews.deleteTheme),
    path('detailTheme/<int:id>', ThemeViews.detailTheme),
    path('updateTheme/<int:id>', ThemeViews.updateTheme),

    #URLs para CDUs Temas
    path('listRent/', RentViews.listRent),
    path('formRent/', RentViews.formRent),
    path('saveRent/', RentViews.saveRent),
    path('deleteRent/<int:id>', RentViews.deleteRent),
    path('detailRent/<int:id>', RentViews.detailRent),
    path('updateRent/<int:id>', RentViews.updateRent),
]