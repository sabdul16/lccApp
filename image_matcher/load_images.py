import os
from pathlib import Path
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_matcher.settings')
django.setup()

from image_app.models import ImageModel  # NOQA

IMG_DIR = Path('G:/LCC_ProjectFinal/image_matcher/')  # update this to your images directory
IMG_FILES = ['color1.png','color2.png','color3.png','color4.png']  # update this to your image file names


def load_images_to_db():
    for i, img in enumerate(IMG_FILES, start=1):
        file_path = IMG_DIR / img
        with open(file_path, 'rb') as img_file:
            ImageModel.objects.create(index=i, image=File(img_file, name=img))


if __name__ == '__main__':
    load_images_to_db()
