from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestJobSearchViewset:

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def test_valid_application_job(self, api_client, test_valid_login):
        data = {
            'token': test_valid_login["token"],
            'post_id': '1',
        }
        response = api_client.post('/job/search-jobs/', data=data, format='json')
        assert response.status_code == status.HTTP_200_OK
