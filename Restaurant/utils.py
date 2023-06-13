from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken


def generate_jwt_token(user):
    token = AccessToken.for_user(user)
    return str(token)


def authentication_user(username, password):
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            return generate_jwt_token(user)
        else:
            return None
    except User.DoesNotExist:
        return None
