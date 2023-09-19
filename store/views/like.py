import jwt
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAuthenticated, IsClientUser
from PixelAlchemy.settings import SECRET_KEY

from ..models import Like
from ..serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):

    def get_permissions(self):
        # FIXME: fix the permissions so the only client can like images .
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsClientUser()]
        return []

    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_permissions(self):
        # FIXME: fix the permissions so the only client can like images .
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return []
        return []

    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class IsLikedByUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, image_id):
        token = request.headers.get('Authorization')
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        like_count = Like.objects.filter(image_id=image_id, user_id=payload['id']).count()
        return Response({'isLiked': like_count > 0})


class DisLikeImage(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, image_id):
        token = request.headers.get('Authorization')
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        like_count = Like.objects.filter(image_id=image_id, user_id=payload['id'])
        like_count.delete()
        return Response({'message': 'image deleted successfully'})


class CountLike(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, image_id):
        like_count = Like.objects.filter(image_id=image_id).count()
        return Response({'numberLikes': like_count})
