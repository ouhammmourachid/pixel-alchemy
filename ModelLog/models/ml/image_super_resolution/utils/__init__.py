import numpy as np
from PIL import Image


def load_image(path):
    img = Image.open(path)
    was_grayscale = len(img.getbands()) == 1
    if was_grayscale or len(img.getbands()) == 4:
        img = img.convert('RGB')
    return was_grayscale, np.array(img)
