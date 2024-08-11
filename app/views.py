from django.shortcuts import render

# Create your views here.
# image_generator/views.py
from django.http import JsonResponse
from .tasks import generate_image

def generate_images(request):
    prompts = ["A red flying dog", "A piano ninja", "A footballer kid"]
    tasks = [generate_image.delay(prompt) for prompt in prompts]
    results = [task.get() for task in tasks]
    return JsonResponse({"images": results})
