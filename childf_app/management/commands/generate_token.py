
from django.core.management.base import BaseCommand
from childf_app.utils import create_super_user
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'generate token'

    def add_arguments(self, parser):
        print(" ")

    def handle(self, *args, **options):
        create_super_user()
        user = User.objects.filter(username='admin')
        token = Token.objects.filter(user=user[0])
        print(token[0].key)
