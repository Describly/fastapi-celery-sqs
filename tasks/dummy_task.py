from celery_app.utils import create_celery
from core.config import get_settings

settings = get_settings()

celery = create_celery()

@celery.task(name="dummy_task", bind=True, max_retries=3, queue="describly-queue-2")
def dummy_task(self, **kwargs):
    print(f"Dummy Task (describly-queue-2): {kwargs}")