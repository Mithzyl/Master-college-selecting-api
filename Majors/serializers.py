from rest_framework import serializers
from Majors.models import Majors


class MajorsSerializer(serializers.ModelSerializer):
    """
    Serializer for majors
    """
    class Meta:
        model = Majors
        fields = '__all__'
        read_only_fields = ('id', 'classes', 'code', 'name')


class ForeignKeyMajorsSerializer(serializers.ModelSerializer):
    """
    Serializer for foreign key of majors
    """
    class Meta:
        model = Majors
        fields = '__all__'
