import os
from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, mobile, password, email=None, **extra_fields):
        """
        Creates and saves a user with given mobile phone number and password
        :param email:
        :param mobile:
        :param password:
        :param extra_fields:
        :return:
        """
        if not mobile:
            raise ValueError("Must provide a 11-num mobile number")
        if email:
            user = self.model(mobile=mobile,
                              email=self.normalize_email(email),
                              **extra_fields)
        else:
            user = self.model(mobile=mobile,
                              **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, mobile, password):
        user = self.model(mobile=mobile, password=password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model
    """
    SEX_CHOICE = (
        (0, '男'),
        (1, '女')
    )
    name = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=11, primary_key=True)
    gender = models.IntegerField(choices=SEX_CHOICE, null=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    college = models.CharField(max_length=40, null=True, blank=True)
    # icon = models.ImageField(null=True, upload_to='static')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "mobile"

