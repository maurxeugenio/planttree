from django import forms
from apps.plants.models import PlantedTree


class PlantForm(forms.ModelForm):
    class Meta:
        model = PlantedTree
        fields = ['tree', 'latitude', 'longitude']
        widgets = {"user": forms.HiddenInput()}
