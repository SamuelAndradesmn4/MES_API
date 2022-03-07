from dataclasses import field, fields
from rest_framework import serializers
from production.models import Pallet, Box

class PalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pallet
        fields = ['Palletqty','line','operator','data_production','shift_closed']

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'