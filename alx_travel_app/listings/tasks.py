from celery import shared_task

@shared_task
def send_notification():
    print("Sending Notification...")
    return "Done"
