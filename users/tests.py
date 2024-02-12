from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import User
import json

class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user_data = {
            "username": "testuser@example.com",
            "password": "testpassword"
        }

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser@example.com')

    def test_login_user(self):
        self.test_register_user()  # Register a user first
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('jwt' in json.loads(response.content)['data'])

    def test_login_user_wrong_password(self):
        self.test_register_user()  # Register a user first
        self.user_data['password'] = 'wrongpassword'  # Use wrong password
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
