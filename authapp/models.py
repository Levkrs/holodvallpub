from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.db import models

# Create your models here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.timezone import now

from holodvall import settings
import secrets

def get_activation_key_expires():
    return now() + timedelta(hours=48)


class ValAuth(AbstractUser):
    username_validator = ASCIIUsernameValidator()

    username = models.CharField(
        "Username",
        max_length=150,
        unique=True,
        help_text=("Required. 150 characters or fewer. Letters, and digits only."),
        # customize the above string as you want
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    email = models.EmailField(verbose_name='email address', blank=True, unique=True)
    # email = models.EmailField(('email address'), blank=True, unique=True)
    companyName = models.CharField(verbose_name='Компания', max_length=128, null=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=get_activation_key_expires)
    unic_token = models.CharField(max_length=8 ,default=secrets.token_hex(4), unique=True, null=True)


    def is_activation_key_expired(self):
        return now() > self.activation_key_expires


    def send_verify_mail(self):
        verify_link = reverse(
            'authapp:verify',
            kwargs={
                'email': self.email,
                'activation_key': self.activation_key,
            },
        )
        title = f'Подтверждение учетной записи {self.username}'
        message = f'Для подтверждения учетной записи {self.username} на портале ' \
                  f'{settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

        html_content = render_to_string('registration/confirm_registration.html', {'domain':settings.DOMAIN_NAME,
                                                                                   'verlink':verify_link,
                                                                                   'username':self.username
                                                                                   })

        return send_mail(title, message, settings.EMAIL_HOST_USER, [self.email], html_message=html_content, fail_silently=False)




class ClientProfile(models.Model):
    user = models.OneToOneField(ValAuth, on_delete=models.CASCADE, primary_key=True)
