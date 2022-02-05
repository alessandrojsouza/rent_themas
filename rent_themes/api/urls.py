from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

#ViewSets routers
router = DefaultRouter()
router.register('themes',ThemeViewSet)
router.register('clients', ClientViewSet)
router.register('itens', ItemViewSet)
router.register('rents', RentViewSet)

#URLs view
urlpatterns = [
     # path('', view_metodo),
]

urlpatterns += router.urls