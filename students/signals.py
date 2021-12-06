from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Student


@receiver(post_save, sender=Student)
def student_created(sender, instance, created, **kwargs):
    if created:
        subject = 'Hello message/do not reply'
        message = f'Dear {instance.name}. Welcome to our school'
        from_email = settings.EMAIL_HOST_USER
        to_list = [instance.email]
        send_mail(
            subject=subject, message=message, from_email=from_email, recipient_list=to_list, fail_silently=False
        )
