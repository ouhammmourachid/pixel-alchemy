from rest_framework import generics

from accounts.permissions import IsClientUser

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
