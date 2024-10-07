import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transparency_kenya.settings')

app = Celery('transparency_kenya')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
