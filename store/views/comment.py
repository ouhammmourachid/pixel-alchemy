from rest_framework import generics

from ..models import Comment
from ..serializers import CommentSerializer


class CommentList(generics.ListCreateAPIView):

    def get_permissions(self):
        # FIXME: fix the permissions so just the owner can delete and update his own comment .
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return []
        return []

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_permissions(self):
        # FIXME: fix the permissions so just the owner can delete and update his own comment .
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return []
        return []

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
