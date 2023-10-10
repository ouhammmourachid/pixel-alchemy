import os

from django.conf import settings
from django.utils import timezone
from PIL import ImageOps

from store.models import Image

from .datasets.div2k.parameters import Div2kParameters
from .models.pretrained import pretrained_models
from .models.srresnet import build_srresnet
from .utils import load_image
from .utils.config import config
from .utils.prediction import get_sr_image


class SuperResolutionModel:

    def __init__(self, model_name: str):

        dataset_key = 'bicubic_x4'
        data_path = config.get('data_path', '')
        div2k_folder = os.path.abspath(os.path.join(data_path, 'div2k'))
        dataset_parameters = Div2kParameters(dataset_key, save_data_directory=div2k_folder)

        self.model_name = model_name
        self.model_key = f'{model_name}_{dataset_key}'
        self.model = build_srresnet(scale=dataset_parameters.scale)

        weights_file = os.path.join(settings.WEIGHTS_DIR, f'{self.model_key}/generator.h5')

        self.model.load_weights(weights_file)

    def predict(self, image_id, user):
        print(self.model)
        timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
        image = Image.objects.get(id=image_id)
        image_path = os.path.join(settings.MEDIA_ROOT, str(image.imagePath))
        # make prediction.
        was_grayscale, lr = load_image(image_path)
        sr = get_sr_image(self.model, lr)
        if was_grayscale:
            sr = ImageOps.grayscale(sr)
        # save the image
        image_extension = image_path.split('.')[-1]
        new_image_name = f'images/image-{timestamp}{image_extension}'
        img_path = os.path.join(settings.MEDIA_ROOT, new_image_name)
        sr.save(img_path)

        super_resolution_image = Image(
            imagePath=new_image_name, description=f'this is a super resolution of the image {image_path}', user=user
        )
        super_resolution_image.save()
        return super_resolution_image


super_resolution_model = SuperResolutionModel('srgan')
