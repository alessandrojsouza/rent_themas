from django.urls import path

from . import views

urlpatterns= [
    path('', views.index),
    path('formClient/', views.formClient),
    path('saveClient/', views.saveClient),
    path('deleteClient/<int:id>', views.deleteClient),
    path('detailClient/<int:id>', views.detailClient),
    path('updateClient/<int:id>', views.updateClient),

]