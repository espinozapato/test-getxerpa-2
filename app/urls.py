from django.urls import path, include
from rest_framework import routers
from .views import CategoriaViewSet, TransaccionViewSet

router = routers.DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('transacciones', TransaccionViewSet)

urlpatterns = [
    path('', include(router.urls)),

]