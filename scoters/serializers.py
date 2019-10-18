from rest_framework import serializers
from .models import Scoters


class ScotersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Scoters
        fields = ['id', 'lat', 'lng', 'is_reserved']
