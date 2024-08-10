from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from .models import EduModel


class EduModelAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@example.com', password='testpassword'
                                        )
        self.client.force_authenticate(user=self.user)
        self.model_data = EduModel.objects.create(
            number=2,
            name='Test Model',
            description='This is a test model')

    def test_get_model_data_details(self):
        url = reverse("educmodels:educmodels-detail", args=(self.model_data.pk,))
        response = self.client.get(url)
        print(response.json())
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['number'], self.model_data.number)
        self.assertEqual(data['name'], self.model_data.name)
        self.assertEqual(data['description'], self.model_data.description)


