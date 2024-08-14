from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class UserTestCase(APITestCase):
    """
    Test User Model and API views
    """

    def setUp(self):
        self.user = User.objects.create(email="test@example.com", is_active=True)
        self.user.set_password("testpassword")

        self.user.save()
        # self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """
        Test creating a new user.
        """
        url = reverse("users:users-list")
        self.data = {"email": "test1@bk.ru", "password": 1234}
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)

    def test_get_user_details(self):
        """
        Test retrieving user details.
        """
        url = reverse("users:users-detail", args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["email"], self.user.email)
        self.assertEqual(data["password"], self.user.password)

    def test_get_list_of_users(self):
        """
        Test retrieving a list of users.
        """
        self.url = reverse("users:users-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_update(self):
        """
        Test updating user details.
        """
        url = reverse("users:users-detail", args=(self.user.pk,))
        data = {"email": "test1@bk.ru", "password": 1234}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("email"), "test1@bk.ru")
        self.assertEqual(data.get("password"), 1234)

    def test_user_delete(self):
        """
        Test deleting a user.
        """
        url = reverse("users:users-detail", args=(self.user.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_token_of_users(self):
        """
        Test obtaining a token for a user.
        """
        url = reverse("users:token_obtain_pair")
        data = {"email": "test@example.com", "password": "testpassword"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
