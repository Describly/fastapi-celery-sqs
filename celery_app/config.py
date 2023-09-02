from kombu import Queue
from core.config import get_settings as app_settings

settings = app_settings()



class BaseSettings:
    """Celery Configuration"""
    
    broker_url = 'sqs://'
    result_backend = None
    broker_transport = "sqs"
    task_default_queue = 'default'
    task_queues = (
        Queue("describly-queue-1"),
        Queue("describly-queue-2"),
    )
    
    broker_transport_options = {
        'region': 'ap-south-1'
    }
    
    worker_concurrency = 1
    
    inlude: list = ['tasks']
    
def get_settings():
    return BaseSettings()