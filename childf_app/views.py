from django.shortcuts import render
import requests
# Create your views here.


def homepage(request):

    return render(request, "homepage.html", {})


