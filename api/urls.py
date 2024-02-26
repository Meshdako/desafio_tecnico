from django.urls import path, include
from rest_framework import routers
from .views import *
from api import views

router = routers.DefaultRouter()
router.register(r'word', views.WordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('inicio', Inicio, name="inicio"),
    path('resultado/<int:id>', Resultado, name="resultado"),
]
