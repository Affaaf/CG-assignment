from rest_framework import status
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestJobSearchViewset:

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def test_valid_job_search(self, api_client, test_valid_login):
        data = {
            'token': test_valid_login["token"]
        }
        response = api_client.get('/job/search-jobs/', data=data, format='json')
        assert response.status_code == status.HTTP_200_OK

    @pytest.fixture
    def test_Invalid_job_search(self, api_client):
        data = {
            'token': 'werttcgvb345678dfghsertdgv'
        }
        response = api_client.get('/job/search-jobs/', data=data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
