from django.shortcuts import render
from rest_framework import generics, filters
from .models import Recipe, Ticket, Sector
from .serializers import RecipeSerializer, TicketSerializer, SectorSerializer

# Create your views here.

class RecipeAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class TicketAPIView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends= [filters.OrderingFilter]
    ordering_fields = "__all__"
    ordering = ['-active']

class TicketUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class SectorAPIView(generics.ListAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class ClosedTicketAPIView(generics.ListAPIView):
    queryset = Ticket.objects.filter(active = False)
    serializer_class = TicketSerializer

class SectorAPIView(generics.ListCreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class SingleTicketApiView(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer