from __future__ import absolute_import, unicode_literals
from datetime import timedelta
from celery import Celery
from django.conf import settings
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miio.settings')

app = Celery('miio')
app.conf.enable_utc = False

app.conf.update(timezone = 'America/Sao_Paulo')

app.config_from_object(settings, namespace='CELERY')

#CELERY BEAT - FOR SCHEDULE TASK
app.conf.beat_schedule = {
    'fetch_popular_movies': {
        'task': 'api.tasks.fetch_api_popular_movies',
        'schedule': timedelta(hours=2)
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
