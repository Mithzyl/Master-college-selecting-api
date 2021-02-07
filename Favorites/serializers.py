from django.utils import timezone
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from Favorites.models import FavoriteColleges, FavoriteMajors


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Base serializer for Favorites
    """
    # set current_user when collect
    current_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    queryset = serializers.ModelSerializer

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
    class Meta:
        model = FavoriteColleges
        fields = '__all__'
        queryset = FavoriteColleges.objects.all()


class FavoriteMajorsSerializer(serializers.ModelSerializer):
    """
    Serializer for Favorite Majors
    """

    class Meta:
        model = FavoriteMajors
        fields = ('base', 'user', 'add_time')
        queryset = FavoriteMajors.objects.all()
