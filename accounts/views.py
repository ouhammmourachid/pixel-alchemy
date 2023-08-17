import datetime

import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from PixelAlchemy.settings import SECRET_KEY

from .models import Tokens, User
from .permissions import IsAuthenticated
from .serializers import UserSerializer


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found !!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password !!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }

        token = jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256',
        )

        # save the token in the token tables
        token_obj, created = Tokens.objects.get_or_create(user=user)
        token_obj.token = token
        token_obj.save()

        # create the response
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token,
        }
        return response


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = request.COOKIES.get('jwt')
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id = payload['id']
            user = User.objects.get(pk=user_id)
            token_obj = Tokens.objects.get(user=user)
            token_obj.delete()
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        response = Response()
        response.delete_cookie('jwt')
        response.data = {'message': 'success'}
        return response