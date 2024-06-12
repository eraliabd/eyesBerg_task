from rest_framework import serializers
from .models import Logo, ConferenceSection


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['id', 'title', 'logo']


class ConferenceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceSection
        fields = ['id', 'title', 'description', 'logo']
