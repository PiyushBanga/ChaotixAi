

# Create your models here.
# image_generator/models.py
from django.db import models

class GeneratedImage(models.Model):
    prompt = models.CharField(max_length=255)
    image_url = models.URLField()
