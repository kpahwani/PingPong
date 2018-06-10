from rest_framework import serializers
from .models import Players


class PlayersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Players
        fields = '__all__'
