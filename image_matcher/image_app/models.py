# image_app/models.py

from django.db import models


class ImageModel(models.Model):
    index = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')
