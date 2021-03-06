from abc import ABC

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from Users.models import User


class UserRegisterSerializer(serializers.Serializer):
    """
    Serializer for the User object
    """
    class Meta:
        model = User
        fields = ('mobile', 'password')
        extra_kwargs = {'password': {'write_only': True}, }

    mobile = serializers.CharField(label="mobile", help_text="mobile number", allow_blank=False, required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all(),
                                                               message="mobile number already exists")])

    password = serializers.CharField(label='password', help_text='password', style={'input_type': 'password'})

    def create(self, validated_data):
        """
        Create a new user with encrypted password
        :param validated_data:
        :return:
        """
        # user = super(UserSerializer, self).create(validated_data=validated_data)
        print(validated_data)
        user = User.objects.create_user(validated_data['mobile'],
                                        validated_data['password'])
        # user.set_password(validated_data['password'])
        # user.save()

        return user


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serialize a user detail
    """
    class Meta:
        model = User
        fields = ('mobile', 'name', 'gender', 'email', 'college')
        extra_kwargs = {'mobile': {'read_only': True}}


class ForeignKeyUserSerializer(serializers.ModelSerializer):
    """
    Serializer for user foreign key
    """
    class Meta:
        model = User
        fields = ('mobile', )
