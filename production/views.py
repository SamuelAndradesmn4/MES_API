from rest_framework import viewsets
from production.models import Pallet, Box
from production.serializer import PalletSerializer, BoxSerializer

class PalletsViewSet(viewsets.ModelViewSet):
    queryset = Pallet.objects.all()
    serializer_class = PalletSerializer

class BoxsViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer