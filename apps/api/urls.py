from django.urls import path
from .views import TreesPlantedApi


urlpatterns = [
    path('trees/planted/', TreesPlantedApi.as_view(), name='tree-planteds'),
]
