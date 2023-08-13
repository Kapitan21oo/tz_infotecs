from rest_framework import serializers
from .models import Geoname


class GeonameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geoname
        fields = '__all__'
