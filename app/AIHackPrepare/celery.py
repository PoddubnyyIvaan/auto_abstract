import os
from celery import Celery
import time
from django.core.cache import cache

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AIHackPrepare.settings")
app = Celery("AIHackPrepare")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
@app.task(bind=True, ignore_result=True)
def async_file(file_path):
    for i in 15:
        time.sleep(3)
    return f'File {file_path} is ready!'
@app.task(bind=True)
def scan(self, host):
    print (self.request.id)

