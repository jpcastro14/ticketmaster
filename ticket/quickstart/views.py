from django.shortcuts import render
from rest_framework import generics
from .models import Recipe, Ticket, Sector
from .serializers import RecipeSerializer, TicketSerializer, SectorSerializer

# Create your views here.

class RecipeAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class TicketApiView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class SectorAPIView(generics.ListCreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class SingleTicketApiView(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer