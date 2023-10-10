from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from store.serializers import ImageSerializer

from .models import History, Operation
from .models.ml import style_transfer, super_resolution_model


class StyleOperationView(APIView):

    def post(self, request):
        data_dict = request.data

        user = User.objects.get(id=data_dict.get('userId'))
        stylized_image = style_transfer.predict(data_dict.get('contentId'), data_dict.get('styledId'), user)
        serializer = ImageSerializer(stylized_image)
        operation = Operation(
            operation='arbitrary-image-stylization-v1-256/2',
            firstImage_id=data_dict.get('contentId'),
            secondImage_id=data_dict.get('styledId')
        )
        operation.save()
        history = History(user=user, resultImage=stylized_image, operation=operation)
        history.save()
        return Response(serializer.data)


class EnhanceQualityOperationView(APIView):

    def post(self, request):
        data_dict = request.data

        user = User.objects.get(id=data_dict.get('userId'))
        super_resolution_image = super_resolution_model.predict(data_dict.get('imageId'), user)

        serializer = ImageSerializer(super_resolution_image)
        operation = Operation(
            operation='image-super-resolution-SRRestNet-SRGAN',
            firstImage_id=data_dict.get('imageId'),
            secondImage_id=None
        )
        operation.save()
        history = History(user=user, resultImage=super_resolution_image, operation=operation)
        history.save()
        return Response(serializer.data)
