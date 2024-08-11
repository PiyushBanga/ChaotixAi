# Chaotix.AI: Django and Celery Integration

This project demonstrates how to create a Django application that generates images using Stability AI's Text-to-Image API. The image generation tasks are handled asynchronously using Celery and Redis as the message broker. This README provides detailed instructions for setting up the environment, running the application, and managing the image generation process.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Optional Task](#optional-task)
- [Project Structure](#project-structure)
- [License](#license)

## Prerequisites
- Python 3.8+
- Django 3.0+
- Celery 5.0+
- Redis (if using Redis as the broker)
- Stability AI API account

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ChaotixAI.git
cd ChaotixAI

python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate


pip install -r requirements.txt


### 2. Run These Commands line by line
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
redis-server
celery -A ChaotixAI worker -l info

```bash
### 3. Hit the endpoint and generate the url
http://127.0.0.1:8000/generate-images/