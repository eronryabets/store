import uuid
from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now

from users.models import EmailVerification, User


@shared_task(name='mail_verification')
def send_mail_verification(user_id):
    print("TEST SUCCESSFUL")
    user = User.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(),
                                              user=user, expiration=expiration)
    record.send_verification_email()
