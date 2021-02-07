from rest_framework import serializers
from Majors.models import Majors


class MajorsSerializer(serializers.ModelSerializer):
    """
    Serializer for majors
    """
    class Meta:
        model = Majors
        fields = "__all__"
        read_only_fields = ('id', 'classes', 'code', 'name')
