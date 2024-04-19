from PIL import Image
from .models import ImageModel
import skimage
from skimage.metrics import structural_similarity as ssim
from skimage.transform import resize
import numpy as np


def calculate_average_color(image):
    img = image
    width, height = img.size
    total_r = total_g = total_b = 0
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            total_r += r
            total_g += g
            total_b += b
    num_pixels = width * height
    avg_r = total_r // num_pixels
    avg_g = total_g // num_pixels
    avg_b = total_b // num_pixels
    return avg_r, avg_g, avg_b


def compare_images(image_file):
    input_image = Image.open(image_file).convert('RGB')
    r, g, b = calculate_average_color(input_image)
    if g >= r and g >= b:
        best_fit_index = -1
        max_ssim = -1
        for image_model in ImageModel.objects.all():
            image = Image.open(image_model.image.path).convert('RGB')
            ref_image = skimage.color.rgb2gray(np.array(input_image))
            image = skimage.color.rgb2gray(np.array(image))
            image = resize(image, ref_image.shape)
            similarity = ssim(ref_image, image, data_range=1.0)

            if similarity > max_ssim:
                max_ssim = similarity
                best_fit_index = image_model.index

        return best_fit_index+1 if max_ssim != -1 else 100
    else:
        return 400
