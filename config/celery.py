import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the celery program
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

# Celery related configuration keys should have a "CELERY_" prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "send_vocabulary": {
        "task": "mainbot.tasks.send_vocabulary",
        "schedule": crontab(minute=0, hour="9,15,22")
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")