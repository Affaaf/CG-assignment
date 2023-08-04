import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
@pytest.mark.django_db
def signup_valid_user():
    user = User.objects.create(
        username='amir',
        first_name='Amir',
        last_name='Umer',
        email='amir@gmail.com',
        password='12345678',
    )
    return {"user": user}

@pytest.fixture
def test_valid_login(self, api_client, signup_valid_user):
    response = api_client.post(
        '/auth/login/',
        {
            "email": signup_valid_user.get("user").email,
            "password": signup_valid_user.get("user").password
        },
        format='json'
    )
    token = response.data.get('access')
    return {"token": token}
