from rest_framework import status
from rest_framework.test import APIClient
import pytest
from django.conf import settings


@pytest.mark.django_db
class TestLoginViewset:

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def test_valid_login(self, api_client, signup_valid_user):
        response = api_client.post(
            '/auth/login/',
            {
                "email":signup_valid_user.get("user").email,
                "password":signup_valid_user.get("user").password
            },
            format='json'
        )
        assert response.status_code == status.HTTP_200_OK

    @pytest.fixture
    def test_invalid_login(self, api_client):
        data = {
            'username': 'air',
            'email': 'amr@gmail.com',
            'password': '12345678',
        }
        response = api_client.post('/auth/login/', data=data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
