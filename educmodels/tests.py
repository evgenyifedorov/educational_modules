from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import Group


from users.models import User
from educmodels.models import EduModel, Lesson


class EduModelTestCase(APITestCase):
    """
    Test EduModel CRUD operations.
    """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email="test@example.com", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)
        self.model_data = EduModel.objects.create(
            number=1,
            name="Test Model",
            description="This is a test model",
            owner=self.user,
        )
        self.lesson = Lesson.objects.create(
            title="test1",
            content="This is a test lesson",
            model=self.model_data,
            owner=self.user,
        )
        self.user1 = User.objects.create(
            email="test1@example.com", password="testpassword"
        )
        self.group = Group.objects.create(name="moderator")
        self.user1.groups.add(self.group)

    def test_educmodel_create(self):
        """
        Test creating a new educational model.
        """
        url = reverse("educmodels:educmodels-list")
        data = {
            "number": "2",
            "name": "Test Model2",
            "description": "This is a test model",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EduModel.objects.all().count(), 2)

    def test_get_educmodel_details(self):
        """
        Test retrieving details of a specific educational model.
        """
        url = reverse("educmodels:educmodels-detail", args=(self.model_data.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["number"], self.model_data.number)
        self.assertEqual(data["name"], self.model_data.name)
        self.assertEqual(data["description"], self.model_data.description)

    def test_get_list_of_educmodel(self):
        """
        Test retrieving a list of educational models.
        """
        self.url = reverse("educmodels:educmodels-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_educmodel_update(self):
        """
        Test updating details of a specific educational model.
        """
        url = reverse("educmodels:educmodels-detail", args=(self.model_data.pk,))
        data = {"name": "Test Model3"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Test Model3")

    def test_educmodel_delete(self):
        """
        Test deleting a specific educational model.
        """
        url = reverse("educmodels:educmodels-detail", args=(self.model_data.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_and_educmodel_add(self):
        """
        Test adding a lesson to an educational model.
        """
        self.url = reverse("educmodels:educmodels-list")
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_perform_create_educmodel(self):
        """
        Test that a user can create a new educational model and that the created model has the correct owner.
        """
        url = reverse("educmodels:educmodels-list")
        data = {
            "number": "2",
            "name": "Test Model2",
            "description": "This is a test model",
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        course = EduModel.objects.get(name="Test Model2")
        self.assertEqual(course.owner, self.user)


class LessonTestCase(APITestCase):
    """
    Test Lesson CRUD operations.
    """

    def setUp(self):

        self.client = APIClient()
        self.user = User.objects.create(
            email="test@example.com", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)
        self.model_data = EduModel.objects.create(
            number=1,
            name="Test Model",
            description="This is a test model",
            owner=self.user,
        )
        self.lesson = Lesson.objects.create(
            title="test1",
            content="This is a test lesson",
            model=self.model_data,
            owner=self.user,
        )
        self.user1 = User.objects.create(
            email="test1@example.com", password="testpassword"
        )
        self.group = Group.objects.create(name="moderator")
        self.user1.groups.add(self.group)

    def test_lesson_create(self):
        """
        Test creating a new lesson.
        """
        url = reverse("educmodels:create_lesson")
        data = {"title": "test3", "content": "name test3", "model": self.model_data.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_get_lesson_details(self):
        """
        Test retrieving details of a specific lesson.
        """
        url = reverse("educmodels:retrieve_lesson", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["title"], self.lesson.title)
        self.assertEqual(data["content"], self.lesson.content)

    def test_get_list_of_lesson(self):
        """
        Test retrieving a list of lessons.
        """
        self.url = reverse("educmodels:lesson_list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_update(self):
        """
        Test updating details of a specific lesson.
        """
        url = reverse("educmodels:update_lesson", args=(self.lesson.pk,))
        data = {"title": "test4"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "test4")

    def test_lesson_delete(self):
        """
        Test deleting a specific lesson.
        """
        url = reverse("educmodels:destroy_lesson", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_and_lesson_add(self):
        """
        Test adding a lesson to an educational model.
        """
        self.url = reverse("educmodels:lesson_list")
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_perform_create_lesson(self):
        """
        Test that a user can create a new lesson and that the created lesson has the correct owner.
        """
        self.url = reverse("educmodels:create_lesson")
        self.data = {
            "title": "test3",
            "content": "name test3",
            "model": self.model_data.pk,
        }
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        lesson = Lesson.objects.get(title="test3")
        self.assertEqual(lesson.owner, self.user1)
