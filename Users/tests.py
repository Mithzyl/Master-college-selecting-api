from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient #make request to api
from rest_framework import  status

CREATE_USER_URL = reverse("users:create")


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
        user = get_user_model().objects.all()
        self.assertTrue(user.check_password(), payload['password'])
        self.assertNotIn("password", res.data)