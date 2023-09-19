import os

import jwt
from django.conf import settings
from django.http import FileResponse, Http404
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAuthenticated
from PixelAlchemy.settings import SECRET_KEY

from ..models import Image
from ..serializers import ImageSerializer


class ImageUploadView(APIView):

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE', 'GET']:
            return [IsAuthenticated()]
        return []

    def post(self, request, format=None):  # noqa
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):  # noqa
        mine_param = request.GET.get('mine')
        all_images = []
        if mine_param == '1':
            token = request.headers.get('Authorization')
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('Unauthenticated!')

            all_images = Image.objects.filter(user_id=payload['id'])
        else:
            all_images = Image.objects.filter(isPrivate=False)
        serializer = ImageSerializer(all_images, many=True)
        return Response(serializer.data)


class ImageCRUDView(APIView):

    def get_permissions(self):
        # FIXME: fix the permissions so that only the owner of the image can edit and delete it .
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return []
        return []

    def get_object(self, image_id):
        try:
            return Image.objects.get(id=image_id)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, image_id, format=None):  # noqa
        image = self.get_object(image_id)
        response = FileResponse(image.imagePath, content_type='image/jpeg')
        return response

    def delete(self, request, image_id, format=None):  # noqa
        image = self.get_object(image_id)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, image_id, format=None):  # noqa
        image = self.get_object(image_id)

        # Delete the old image file from the filesystem
        if image.imagePath:
            old_image_path = os.path.join(settings.MEDIA_ROOT, str(image.imagePath))
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

        serializer = ImageSerializer(image, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
