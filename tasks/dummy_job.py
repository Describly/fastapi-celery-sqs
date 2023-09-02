from celery_app.utils import create_celery
from core.config import get_settings

settings = get_settings()

celery = create_celery()

@celery.task(name="dummy_job", bind=True, max_retries=3, queue="describly-queue-1")
def dummy_job(self, **kwargs):
    print(f"Dummy job (describly-queue-1): {kwargs}")