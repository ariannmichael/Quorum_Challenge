from celery import Celery
from django.conf import settings

app = Celery(
    'backend',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)