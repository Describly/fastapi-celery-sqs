from fastapi import FastAPI
from celery_app.utils import create_celery
from tasks.dummy_job import dummy_job
from tasks.dummy_task import dummy_task


app = FastAPI()
app.celery_app = create_celery()

celery = app.celery_app

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/dummy-job/{query}")
def queue_job(query):
    kwargs = {"query": query}
    dummy_job.apply_async(queue="describly-queue-1", kwargs=kwargs)
    
    


@app.get("/dummy-task/{query}")
def queue_task(query):
    kwargs = {"query": query}
    dummy_task.apply_async(queue="describly-queue-2", kwargs=kwargs)
    
    