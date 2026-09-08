from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class HealthEndpointTests(APITestCase):
    def test_returns_ok_without_authentication(self):
        response = self.client.get(reverse('health'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'status': 'ok'})

    def test_rejects_disallowed_method(self):
        response = self.client.post(reverse('health'))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class JWTAuthTests(APITestCase):
    def setUp(self):
        self.username = 'alice'
        self.password = 's3cret-pass'
        self.user = get_user_model().objects.create_user(
            username=self.username, password=self.password
        )

    def test_obtain_token_pair_with_valid_credentials(self):
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_obtain_token_pair_with_invalid_credentials(self):
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': self.username,
            'password': 'wrong-password',
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access', response.data)

    def test_refresh_token_with_valid_refresh(self):
        obtain = self.client.post(reverse('token_obtain_pair'), {
            'username': self.username,
            'password': self.password,
        })
        response = self.client.post(reverse('token_refresh'), {
            'refresh': obtain.data['refresh'],
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_refresh_token_with_invalid_refresh(self):
        response = self.client.post(reverse('token_refresh'), {
            'refresh': 'not-a-real-token',
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
