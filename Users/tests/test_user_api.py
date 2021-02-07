from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient  # make request to api
from rest_framework import status
from Users.models import User

CREATE_USER_URL = reverse("users_create-list")
TOKEN_URL = reverse("create_token")


def create_user(**param):
    return get_user_model().objects.create(param)


class PublicUserApiTests(TestCase):
    """
    Test public user API
    """
    def setUp(self):
        self.client = APIClient()

    def test_create_user_with_valid_data(self):
        payload = {
            'mobile': '17683058706',
            'password': 'huyuan1649'
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertTrue(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        # self.assertNotIn("password", res.data)

    def test_create_token(self):
        payload = {
            'mobile': '17683058706',
            'password': 'huyuan1649'
        }
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)