from django.core.mail import send_mail
from django.conf import settings
def send_email_to_client():
    subject = 'i am a hero'
    messages = 'oi mug pagal'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['9999@gmail.com']
    send_mail(subject, messages, from_email, recipient_list)

