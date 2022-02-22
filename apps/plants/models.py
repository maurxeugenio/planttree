from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Plant(models.Model):
    name = models.CharField(max_length=255, blank=True)
    scientific_name = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return self.name

class PlantedTree(models.Model):
    user = models.ForeignKey('accounts.User',
        related_name='plant_owner', on_delete=models.CASCADE)
    tree = models.ForeignKey(Plant,
        related_name='planted_tree', on_delete=models.CASCADE)
    latitude = models.FloatField(
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)])
    longitude = models.FloatField(
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])
    planted_at = models.DateTimeField(auto_now_add=True)

    def point(self):
        return self.latitude, self.longitude

    def get_age(self):
        days_in_year = 365.2425
        age = int((timezone.now() - self.planted_at).days / days_in_year)
        return age

    def __str__(self):
        return f'Tree: {self.tree} {self.get_age()}'
