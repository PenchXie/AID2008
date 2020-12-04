from test_celery.celery import app
import time


@app.task
def task_test():
    print('task begins...')
    time.sleep(5)
    print('task finishes...')
