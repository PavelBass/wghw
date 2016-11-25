from wghw import celery_app


@celery_app.task
def send_email(email=None, time=None, message=None):
    print(email, time, message)
