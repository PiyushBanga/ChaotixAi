from celery import shared_task
import requests

@shared_task
def generate_image(prompt):
    api_url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
    headers = {
        "Authorization": "Bearer sk-FavBg0PxrlM8NUqsEPNSLTB5cDf7YJ69aZUJcjHncoORQcxe",
        "Content-Type": "application/json"
    }
    payload = {
        "text_prompts": [
            {"text": prompt}
        ],
        "width": 1024,
        "height": 1024,
    }
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()
