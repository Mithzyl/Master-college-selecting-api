from django.utils import timezone
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.validators import UniqueTogetherValidator

from Colleges.models import Colleges
from Favorites.models import FavoriteColleges, FavoriteMajors
from Colleges.serializers import ForeignKeyCollegesSerializer
from Majors.serializers import ForeignKeyMajorsSerializer
from Users.serializers import ForeignKeyUserSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Base serializer for Favorites
    """
    # set current_user when collect
    current_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    add_time = serializers.DateTimeField(format='%Y-%m-%d %H: %M')

    class Meta:
        queryset = serializers.ModelSerializer
        model = None

        # repeating collecting now allowed functions
        validators = UniqueTogetherValidator(
            queryset=queryset,
            fields=('base', 'user'),
            message="Repeating collection"
        )

        fields = ('base', 'user', 'add_time')


class FavoriteCollegesSerializer(serializers.ModelSerializer):
    """
    Serializer for Favorite colleges
    """
    # set current_user when collect
    current_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    add_time = serializers.DateTimeField(format='%Y-%m-%d %H: %M')
    base = ForeignKeyCollegesSerializer()

    class Meta:
        model = FavoriteColleges
        queryset = FavoriteColleges.objects.all()

        # fields = '__all__'
        fields = ('current_user', 'base', 'add_time')

    def create(self, validated_data):

        college, _ = Colleges.objects.get_or_create(name=validated_data['base']['name'])
        fav = Colleges.objects.get(name=college)
        
        fav_college = FavoriteColleges.objects.create(user=validated_data["current_user"],
                                                      base=fav)

        return Response(fav_college, status.HTTP_201_CREATED)



class FavoriteMajorsSerializer(serializers.ModelSerializer):
    """
    Serializer for Favorite Majors
    """
    # set current_user when collect
    current_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    add_time = serializers.DateTimeField(format='%Y-%m-%d %H: %M')
    base = ForeignKeyMajorsSerializer()

    class Meta:
        model = FavoriteMajors
        queryset = FavoriteMajors.objects.all()

        fields = '__all__'
