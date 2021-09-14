from .models import URl 
from rest_framework import serializers

class URlSerializer(serializers.ModelSerializer):
    class Meta:
        model = URl
        fields = ['full_url','short_url']