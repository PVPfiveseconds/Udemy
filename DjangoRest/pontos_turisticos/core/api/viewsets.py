from rest_framework.viewsets import ModelViewSet
from core.models import TouristSpot
from .serializers import TouristSpotSerializer


class TouristSpotViewSet(ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
