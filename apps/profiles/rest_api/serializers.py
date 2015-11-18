__author__ = 'PerminovMA@live.ru'

from rest_framework import serializers
from profiles.models import UserProfile, Client, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ('password', 'is_superuser', 'is_staff', 'is_active')


class UserProfileShortSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'first_name', 'last_name', 'avatar', 'cities')


class ClientSerializer(serializers.ModelSerializer):
    user = UserProfileShortSerializer()

    class Meta:
        model = Client
        exclude = ('id',)