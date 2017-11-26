from django.shortcuts import render
import requests
# Create your views here.


def mainpage(request):

    return render(request, "mainpage.html", {})


