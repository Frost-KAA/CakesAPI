# serializers.py
from rest_framework import serializers

from .models import Cake

class CakeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cake
        fields = ('id', 'name', 'price', 'desc', 'upload')
