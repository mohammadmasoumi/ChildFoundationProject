import random

from django.contrib.auth.models import User
from django.db import models, transaction


# Create your models here.


class HasUserMixin:
    user_relate_name = None
    user = models.OneToOneField('auth.User', related_name=user_relate_name)
    code_melli = models.CharField(max_length=10, unique=True)


class MadadJou(HasUserMixin, models.Model):
    user_relate_name = 'madadjou'



class MadadKar(HasUserMixin, models.Model):
    user_relate_name = 'madadkar'


def random_string():
    return str(random.randint(10000, 99999))


class HamYarManager(models.Manager):
    @transaction.atomic
    def create(self, username, password, email=None, first_name=None, last_name=None, **kwargs):
        print(username)
        print(password)
        print(email)
        print(first_name)
        print(last_name)
        print(kwargs)
        user = User.objects.create_user(username, email, password,
                                        first_name=first_name, last_name=last_name)
        return super(HamYarManager, self).create(user=user, **kwargs)

class HamYar(models.Model):
    user = models.OneToOneField('auth.User', related_name='hamyar')
    code_melli = models.CharField(max_length=10, null=True)
    objects = HamYarManager()
    activation_code = models.CharField(max_length=6, default=random_string)
    job = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(max_length=2, default='1', choices=[
        ('1', 'مذکر'),
        ('2', 'مونث'),
    ])
    education = models.CharField(max_length=2, default='1', choices=[
        ('1', 'بی‌سواد'),
        ('2', 'ابتدایی'),
        ('3', 'دیپلم'),
        ('4', 'لیسانس'),
        ('5', 'فوق‌لیسانس'),
        ('6', 'دکترا'),
    ])
    payment_period = models.IntegerField(null=True, blank=True, choices=[
        (1, '۱ ماهه'),
        (2, '۲ ماهه'),
        (3, '۳ ماهه'),
        (6, '۶ ماهه'),
    ])
