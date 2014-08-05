from celery import task
from django.core.mail import EmailMessage

@task()
def send_email(data):
    email = EmailMessage('Hello', 'World', to=['target@gmail.com'])
    email.send()
