from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend

# This is a variation of what was taught in the class. This one works in Django 3


class EmailAuth(BaseBackend):
    """Authenticate a user by exact match on the email and password"""

    def authenticate(self, request, username=None, password=None):
        """Get an instance of 'User' based on the email and verify password"""

        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        try:
            user = User.objects.get(**kwargs)

            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Used by Django authentication system to retrieve a user instance"""

        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None

        except User.DoesNotExist:
            return None
