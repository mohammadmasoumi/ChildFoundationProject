import random

import datetime
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models, transaction


# Create your models here.


class MadadJou(models.Model):
    last_periodic_request_created_date = models.DateTimeField(null=True, blank=True)
    niaz_mahane = models.IntegerField()
    user = models.OneToOneField('auth.User', related_name='madadjou')
    picture = models.ImageField(upload_to='madadju', null=True, blank=True)
    shomare_parvande = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=2, default='1', choices=[
        ('1', 'مذکر'),
        ('2', 'مونث'),
    ])
    birth_date = models.DateTimeField(null=True, blank=True)
    sharaiet_jesmani = models.CharField(max_length=2, default='1', choices=[
        ('1', 'سالم'),
        ('2', 'معلول'),
    ])
    bimari = models.CharField(max_length=20, null=True, blank=True)
    vaziat_omumi = models.CharField(max_length=20, null=True, blank=True)
    mahal_sokunat = models.CharField(max_length=20, null=True, blank=True)
    malekiat_maskan = models.CharField(max_length=2, default='1', choices=[
        ('1', 'دارد'),
        ('2', 'ندارد'),
    ])
    tedad_otagh = models.IntegerField(null=True, blank=True)
    ejare = models.IntegerField(null=True, blank=True)
    vaziat_sokunat = models.CharField(max_length=20, null=True, blank=True)
    vaziat_eshteghal_pedar = models.CharField(max_length=20, null=True, blank=True)
    vaziat_eshteghal_madar = models.CharField(max_length=20, null=True, blank=True)
    daramad_pedar = models.IntegerField(null=True, blank=True)
    daramad_madar = models.IntegerField(null=True, blank=True)
    shoghl_pedar = models.CharField(max_length=20, null=True, blank=True)
    shoghl_madar = models.CharField(max_length=20, null=True, blank=True)
    tarighe_komake_digar = models.CharField(max_length=2, default='1', choices=[
        ('1', 'دارد'),
        ('2', 'ندارد'),
    ])
    manbae_komake_digar = models.CharField(max_length=20, null=True, blank=True)
    meghdar_komake_digar = models.IntegerField(null=True, blank=True)
    tozihat = models.CharField(max_length=20, null=True, blank=True)
    tahsilat_madar = models.CharField(max_length=20, null=True, blank=True)
    tahsilat_pedar = models.CharField(max_length=20, null=True, blank=True)
    birth_date_madar = models.DateTimeField(null=True, blank=True)
    birth_date_pedar = models.DateTimeField(null=True, blank=True)
    vaziat_jesmani_madar = models.CharField(max_length=2, default='1', choices=[
        ('1', 'سالم'),
        ('2', 'معلول'),
    ])
    vaziat_jesmani_pedar = models.CharField(max_length=2, default='1', choices=[
        ('1', 'سالم'),
        ('2', 'معلول'),
    ])
    bimari_madar = models.CharField(max_length=20, null=True, blank=True)
    bimari_pedar = models.CharField(max_length=20, null=True, blank=True)
    elat_fot_madar = models.CharField(max_length=20, null=True, blank=True)
    elat_fot_pedar = models.CharField(max_length=20, null=True, blank=True)
    ghaiem_feli = models.CharField(max_length=20, null=True, blank=True)
    tedad_baradaran = models.IntegerField(null=True, blank=True)
    tedad_khaharan = models.IntegerField(null=True, blank=True)

    @property
    def age(self):
        return datetime.datetime.now() - self.birth_date


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
    supported_children = models.ManyToManyField('childf_app.MadadJou', related_name='hamian')
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


class HelpRequest(models.Model):
    madadjou = models.ForeignKey('childf_app.MadadJou', related_name='help_requests')
    amount = models.IntegerField()
    is_verified = models.BooleanField(default=False)
    critical = models.BooleanField(default=False)

    @property
    def payed_sum(self):
        return sum([p.amount for p in self.payments.all()])

    @property
    def needed(self):
        return self.amount - self.payed_sum


class MadadPayment(IPayment):
    help_request = models.ForeignKey('childf_app.HelpRequest', related_name='payments')


class Message(models.Model):
    sender = models.ForeignKey('auth.User', related_name='outbox')
    receiver = models.ForeignKey('auth.User', related_name='inbox')
    subject = models.CharField(max_length=100, default='پیام جدید')
    body = models.TextField(null=True, blank=True)
