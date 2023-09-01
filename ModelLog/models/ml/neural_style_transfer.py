import tensorflow_hub as hub

from ModelLog.utils import *
from store.models import Image


class NeuralStyleTransfer:

    def __init__(self):
        self.model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
        print(self.model)

    def predict(self, content_image_pk: int, styled_image_pk: int, user):
        content_image = Image.objects.get(id=content_image_pk)
        styled_image = Image.objects.get(id=styled_image_pk)
        content_image_path = str(content_image.imagePath)
        styled_image_path = str(styled_image.imagePath)
        content_image_array, styled_image_array = load_images(content_image_path, styled_image_path)
        print(self.model)
        stylized_image = self.model(content_image_array, styled_image_array)[0]
        image_path = tensor_to_image(stylized_image, content_image_path, styled_image_path)
        new_image = Image(
            imagePath=image_path,
            description=f'this is a stylized image produced using {content_image_path} and {styled_image_path}',
            user=user
        )
        new_image.save()
        return new_image


style_transfer = NeuralStyleTransfer()
