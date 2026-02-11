from django.shortcuts import render
from rest_framework import generics, filters
from .models import Recipe, Ticket, Sector, Broker
from .serializers import RecipeSerializer, TicketSerializer, SectorSerializer, BrokerSerializer

# Create your views here.

class RecipeAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class TicketAPIView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends= [filters.OrderingFilter]
    ordering_fields = "__all__"
    ordering = ['-created_at']

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

class BrokerAPIView(generics.ListAPIView):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer

class BrokerNewSaleAPIView(generics.RetrieveUpdateAPIView):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer
    