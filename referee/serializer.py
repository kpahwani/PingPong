from rest_framework import serializers
from .models import Championships


class ChampionshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Championships
        fields = '__all__'
