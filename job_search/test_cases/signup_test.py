from rest_framework import status
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestSignupViewset:

    def api_client(self):
        return APIClient()

    def test_valid_signup(self, api_client):
        data = {
            'username': 'amir',
            'first_name': 'Amir',
            'last_name': 'Umer',
            'email': 'amir@gmail.com',
            'password': '12345678'
        }
        response = api_client.post('/auth/signup/', data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_existing_user_signup(self, api_client, signup_valid_user):
        data ={
                "username": signup_valid_user.get("user").username,
                "first_name": signup_valid_user.get("user").first_name,
                "last_name": signup_valid_user.get("user").last_name,
                "email": signup_valid_user.get("user").email,
                "password": signup_valid_user.get("user").password
        }
        response = api_client.post('/auth/signup/', data=data,format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_Invalid_signup(self, api_client):
        data = {
            'username': 'amir',
            'first_name': 'Amir',
            'last_name': 'Umer',
            'email': 'amirgmail.com',
            'password': '12345678',

        }
        response = api_client.post('/auth/signup/', data=data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST


