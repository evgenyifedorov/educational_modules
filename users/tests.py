from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=4,
            email='test@example.com',
            password='testpassword',
        )
        self.client.force_authenticate(user=self.user)


    def test_user_create(self):
        url = reverse("users:users-list")
        data = {"email": "test1@bk.ru", "password": 1234}
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)

    # def test_user_create(self):
    #     url = reverse("users:users-list")
    #     data = {
    #         'email': 'test3@example.com',
    #         'password': 'testpassword1',
    #     }
    #     response = self.client.post(url, data)
    #     print(data)
    #     self.assertEqual(self.user.email, data['email'])
    #     self.assertTrue(self.user.password, data['password'])
    #     self.assertEqual(User.objects.all().count(), 1)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_user_details(self):
        url = reverse("users:users-detail", args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['email'], self.user.email)
        self.assertEqual(data['password'], self.user.password)

    def test_get_list_of_users(self):
        self.url = reverse("users:users-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
