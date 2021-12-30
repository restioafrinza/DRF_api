from django.shortcuts import render
from rest_framework import viewsets

from .serializers import FotoSerializer
from .models import Foto


class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all().order_by('name')
    serializer_class = FotoSerializer
# Create your views here.
