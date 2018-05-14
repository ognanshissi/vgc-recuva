from rest_framework import serializers
from customer.models import CustomerProfile, GroupZone


class CustomerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerProfile
        fields = ['gender', 'first_name', 'last_name', 'category', 'structure_name', 'contact', 'enabled', 'address', 'timestamp', 'updated']


class ZoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupZone
        fields = ['id', 'name', 'group']