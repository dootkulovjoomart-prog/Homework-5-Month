from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from user.models import CustomUser

@shared_task
def hello_task(name):
    from time import sleep
    sleep(10    )
    print(f"Привет {name}")

@shared_task
def send_email_wellcome(email):
    send_mail(
        subject='wellcome' ,
        message='thanks for registrations',
        from_email='admin@gmail.com',
        recipient_list=[email],
        fail_silently= False

    )
    print('email sended')

@shared_task
def delete_email():
    time_limit = timezone.now -  timedelta(days=3)

    deleted_count, _ = CustomUser.objects.filter(
        is_active =False ,
        date_joined_lt = time_limit

    ).delete()

    print(f"Удалено неактивных пользователей: {deleted_count}")