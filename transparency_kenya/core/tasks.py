from celery import shared_task
import requests

@shared_task
def fetch_county_spending():
    response = requests.get('https://www.oagkenya.go.ke/')
    data = response.json()

