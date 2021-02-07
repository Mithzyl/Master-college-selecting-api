from rest_framework import serializers
from Colleges.models import Colleges


class CollegesSerializer(serializers.ModelSerializer):
    """
    Serializer for Colleges
    """
    class Meta:
        model = Colleges
        fields = ('id', 'name', 'province', 'is_211', 'is_985')
        read_only_fields = ('id', 'name', 'province', 'is_211', 'is_985')
