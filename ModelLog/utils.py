import os

import tensorflow as tf
from django.conf import settings
from django.utils import timezone


def tensor_to_image(tensor, first_image_path, second_image_path):
    """Converts a tensor to an image"""
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    tensor_shape = tf.shape(tensor)
    number_elem_shape = tf.shape(tensor_shape)
    if number_elem_shape > 3:
        assert tensor_shape[0] == 1
        tensor = tensor[0]
    img = tf.keras.preprocessing.image.array_to_img(tensor)
    # get images name
    first_base_filename, _ = os.path.splitext(first_image_path.split('/')[-1])
    second_base_filename, _ = os.path.splitext(second_image_path.split('/')[-1])

    # create a new name and the save the image in the media file
    new_file_name = f'image-{timestamp}'
    img_path = os.path.join(settings.MEDIA_ROOT, f'images/{new_file_name}.png')
    img.save(img_path)
    return f'images/{new_file_name}.png'


def load_img(path_to_img):
    """loads an image as a tensor and scales it to 512 pixels"""
    max_dim = 512
    image = tf.io.read_file(path_to_img)
    image = tf.image.decode_jpeg(image)
    image = tf.image.convert_image_dtype(image, tf.float32)

    shape = tf.cast(tf.shape(image)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    image = tf.image.resize(image, new_shape)
    image = image[tf.newaxis, :]

    return image


def load_images(content_path, style_path):
    """loads the content and path images as tensors"""
    content_image = load_img(f'{settings.MEDIA_ROOT}/{content_path}')
    style_image = load_img(f'{settings.MEDIA_ROOT}/{style_path}')

    return content_image, style_image
