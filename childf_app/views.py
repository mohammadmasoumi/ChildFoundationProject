from django.shortcuts import render
import requests
# Create your views here.


def mainpage(request):

    return render(request, "mainpage.html", {})


def development_team(request):
    return render(request, "development_team.html", {})


def history(request):
    return render(request, "history.html", {})


def organizational_chart(request):
    return render(request, 'organizational_chart.html', {})


def goals(request):
    return render(request, 'goals.html', {})


def activities(request):
    return render(request, 'activities.html', {})
