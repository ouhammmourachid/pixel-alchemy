import jwt
from rest_framework import permissions

from PixelAlchemy.settings import SECRET_KEY

from .models import Tokens, User


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        token = request.COOKIES.get('jwt')
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return False

        user = User.objects.filter(id=payload['id']).first()
        return user.role == 'admin'


class IsClientUser(permissions.BasePermission):

    def has_permission(self, request, view):
        token = request.COOKIES.get('jwt')
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return False

        user = User.objects.filter(id=payload['id']).first()
        return user.role == 'client'


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            token = request.COOKIES.get('jwt')
            if not token:
                return False
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id = payload['id']
            user = User.objects.get(pk=user_id)
            token_obj = Tokens.objects.get(user=user)
            print(token_obj.token)
            print(token)
            return token_obj.token == token
        except jwt.ExpiredSignatureError:
            return False
