from django.shortcuts import render
from rest_framework import generics
from .models import Recipe, Ticket
from .serializers import RecipeSerializer, TicketSerializer

# Create your views here.

class RecipeAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class TicketApiView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer