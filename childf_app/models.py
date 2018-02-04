import random
from django.db import models

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


class HamYar(HasUserMixin, models.Model):
    user_relate_name = 'hamyar'
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
        (4, '۴ ماهه'),
    ])
