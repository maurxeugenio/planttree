from django.urls import path
from .views import Dashboard, TreeView, PlantsAccount, PlantTree

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('plant/tree/', PlantTree.as_view(), name='plant_tree'),
    path('tree/account/', PlantsAccount.as_view(), name='plants_account'),
    path('tree/<pk>/', TreeView.as_view(), name='view-tree'),
]
