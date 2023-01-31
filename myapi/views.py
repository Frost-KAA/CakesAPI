from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework import viewsets
from .serializers import CakeSerializer
from .models import Cake


class CakeViewSet(viewsets.ModelViewSet):
    queryset = Cake.objects.all().order_by('name')
    serializer_class = CakeSerializer