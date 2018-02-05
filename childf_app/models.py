import random

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models, transaction


# Create your models here.


class MadadJou(models.Model):
    user = models.OneToOneField('auth.User', related_name='madadjou')
    code_melli = models.CharField(max_length=10, unique=True)


class MadadKar(models.Model):
    user = models.OneToOneField('auth.User', related_name='madadkar')


def random_string():
    return str(random.randint(10000, 99999))


class HamYarManager(models.Manager):
    @transaction.atomic
    def create(self, username, password, email=None, first_name=None, last_name=None, **kwargs):
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


class IPayment(models.Model):
    amount = models.IntegerField(validators=[MinValueValidator(1)])
    payer = models.ForeignKey('auth.User')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BonyadPayment(IPayment):
    pass


class MadadjuPayment(IPayment):
    madadju = models.ForeignKey('childf_app.MadadJou', related_name='payments')
