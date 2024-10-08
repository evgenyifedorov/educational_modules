from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Creates a superuser for the application.
    """

    def handle(self, *args, **kwargs):
        user = User.objects.create(email="admin@bk.com")
        user.set_password("12345678")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
