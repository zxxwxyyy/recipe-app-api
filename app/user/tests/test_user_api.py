"""
Test for the user api
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')


def create_user(**params):
    """Create and return a new user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the public features of the user API"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test if create user is sucessful"""
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }
        result = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', result.data) # For security purpose, password is not in the data returns

    def test_user_with_email_exisits_error(self):
        """Test error return if user with email exists"""
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }
        create_user(**payload)
        result = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test an error is returned if password less than 5 chars"""
        payload = {
            'email': 'test@example.com',
            'password': 'haha',
            'name': 'Test Name',
        }
        result = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email = payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test generates token for valid credentials."""
        user_details = {
            'name': 'Test Name',
            'email': 'test@example.com',
            'password': 'test-password-123',
        }
        create_user(**user_details)

        payload = {
            'email': user_details['email'],
            'password': user_details['password']
        }
        result = self.client.post(TOKEN_URL, payload) # upload payload to the token url

        self.assertIn('token', result.data) # Check if the response includes token
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    def test_create_token_bad_credentials(self):
        """Test returns error if credentials invalid"""
        create_user(email='test@example.com', password ='goodpass')

        payload = {'email':'test@example.com', 'password':'badpass'}
        result = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', result.data)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_blank_password(self):
        """Test posting a blank password return error"""
        payload = {'email': 'test@example.com', 'password': ''}
        result = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', result.data)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)