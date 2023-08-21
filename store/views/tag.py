from rest_framework import generics

from accounts.permissions import IsAdminUser

from ..models import Tag
from ..serializers import TagSerializer


class TagList(generics.ListCreateAPIView):

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAdminUser()]
        return []

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAdminUser()]
        return []

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
