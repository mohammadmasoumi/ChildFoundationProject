import random
from django.db import models

# Create your models here.


class HasUserMixin:
    user_relate_name = None
    user = models.OneToOneField('auth.User', related_name=user_relate_name)


class MadadJou(HasUserMixin, models.Model):
    user_relate_name = 'madadjou'



class MadadKar(HasUserMixin, models.Model):
    user_relate_name = 'madadkar'


def random_string():
    return str(random.randint(10000, 99999))

class HamYar(HasUserMixin, models.Model):
    user_relate_name = 'hamyar'
    activation_code = models.CharField(max_length=6, default=random_string)

