from django.contrib.auth.models import User
from django.conf import settings
import jwt


def generate_jwt_token(user):
    payload = {
        'user_id': user.id,
        'username': user.username,
        'email': user.email,
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='H256')
    return token.decode('utf-8')


def authentication_user(username, password):
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            return generate_jwt_token(user)
        else:
            return None
    except User.DoesNotExist:
        return None
