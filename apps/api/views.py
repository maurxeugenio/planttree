from apps.plants.models import PlantedTree
from rest_framework import status
from rest_framework.views import APIView
from .serializers import TreesPlantedSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TreesPlantedApi(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TreesPlantedSerializer

    def get(self, request):
        serializer = self.serializer_class(PlantedTree.objects.filter(user=self.request.user), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
