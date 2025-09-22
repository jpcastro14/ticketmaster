from rest_framework import serializers

from .models import Recipe, Ticket, Sector

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'

class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = '__all__'

class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = "__all__"