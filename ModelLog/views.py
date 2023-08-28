from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from store.serializers import ImageSerializer

from .models import History, Operation
from .models.ml import style_transfer


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
        history = History(userId=user, resultImage=stylized_image, operationId=operation)
        history.save()
        return Response(serializer.data)
