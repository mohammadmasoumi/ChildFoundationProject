from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
from django.views.decorators.csrf import csrf_exempt
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


def test(request):
    return render(request, 'sidebar test.html', {})


@csrf_exempt
def registration(request):
    return render(request, 'registration.html', {})


def accept_registration_terms(request):
    return render(request, 'accept_registration_terms.html', {})

@csrf_exempt
def activation_code(request):
    return render(request, 'activation_code.html', {})


@csrf_exempt
def resend_sms(request):
    text='کد فعال سازی ارسال شد'
    html = '<p class="swal-text">%s</p>' %text
    return HttpResponse(html)


@csrf_exempt
def send_code(request):
    mobileNo = 123
    resend_sms(mobileNo)


@csrf_exempt
def login(request):
    return render(request, 'login.html', {})


@csrf_exempt
def verification(request):
    if request.is_ajax():
        entered_code = request.POST.get('code', False)
        thanks_msg = ("حساب کاربری شما با موفقیت ساخته شد!")
        redirect_to_home_msg = ("صفحه اصلی خود را ببینید")
        html = '<p class="swal-text">%s</p>' \
               ' <hr> <a class="swal-text" href="/fa-ir/home/">%s </a><br/>' \
                % (thanks_msg, redirect_to_home_msg)
        result = {'result': 1, 'html': html}
        return HttpResponse(json.dumps(result))


@csrf_exempt
def payment(request):
    render((request, 'payment.html', {}))
