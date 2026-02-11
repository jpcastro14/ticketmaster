from rest_framework import serializers

from .models import Recipe, Ticket, Sector, Broker

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = '__all__'

class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = ['id','name','code','description']

class TicketSerializer(serializers.ModelSerializer):

    sector = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Sector.objects.all())
    #sector = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Ticket
        fields = '__all__'


class BrokerSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Broker
        fields = '__all__'