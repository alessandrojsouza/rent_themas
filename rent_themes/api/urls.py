from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

#ViewSets routers
router = DefaultRouter()
#router.register('clients', ClientViewSet)
router.register('itens', ItemViewSet)
router.register('rents', RentViewSet)
router.register('phone', PhoneViewSet)

#URLs view
urlpatterns = [
      path('clients/', ClientViewSet.as_view()),
]

urlpatterns += router.urls