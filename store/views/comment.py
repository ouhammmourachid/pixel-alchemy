from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAuthenticated

from ..models import Comment, Image
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


class CommentCount(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, image_id):
        comment_count = Comment.objects.filter(image_id=image_id).count()
        return Response({'numberComments': comment_count})


class CommentImage(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, image_id):
        image = Image.objects.filter(id=image_id).count()
        if image:
            comments = Comment.objects.filter(image_id=image_id)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        return Response([])
