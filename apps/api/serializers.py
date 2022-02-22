from apps.accounts.models import User
from apps.plants.models import PlantedTree
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class TreesPlantedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = PlantedTree
        fields = ['tree', 'user', 'point', 'planted_at']
        depth = 1
