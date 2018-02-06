# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import json

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def generate_token(request):
    response = {}
    user_for_token = User.objects.get(username="admin")
    token = Token.objects.get(user=user_for_token)
    response["token"] = token.key
    return HttpResponse(json.dumps(response), content_type="application/json")


@api_view(['GET', 'POST'])
def signup(request):
    response = {}
    if request.method == "POST":
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']
        mobile = data['mobile']
        defaults = {"mobile": mobile, "password": password}
        user, created = User.objects.get_or_create(defaults, username=username)

        if created:
            response["code"] = 201
        else:
            response["code"] = 404
        return HttpResponse(json.dumps(response), content_type="application/json")
    return HttpResponse(None)


@api_view(['GET', 'POST'])
def signin(request):
    response = {}
    if request.method == "POST":
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']
        user = User.objects.filter(username=username, password=password)

        if user:
            response['code'] = 200
        else:
            response['code'] = 404
            response['error'] = "username or password is not correct"

        return HttpResponse(json.dumps(response), content_type="application/json")
    return HttpResponse(None)
