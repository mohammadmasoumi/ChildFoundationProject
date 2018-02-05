from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

def create_super_user():
    user = User.objects.filter(username='admin')
    if not user:
        User.objects.create_superuser(username='admin', email='mohammad.masoomy74@gmail.com',
                                      password='admin1234')
        user = User.objects.filter(username='admin')
    token = Token.objects.filter(user=user[0])
    if not token:
        Token.objects.create(user=user[0])
        token = Token.objects.filter(user=user[0])
    token[0].save()