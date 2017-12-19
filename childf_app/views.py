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
    if request.method == 'POST':
        return render(request, 'home.html', {})
    return render(request, 'login.html', {})


@csrf_exempt
def verification(request):
    if request.is_ajax():
        entered_code = request.POST.get('code', False)
        thanks_msg = ("حساب کاربری شما با موفقیت ساخته شد!")
        redirect_to_home_msg = ("صفحه اصلی خود را ببینید")
        html = '<p class="swal-text">%s</p>' \
               ' <hr> <a class="swal-text" href="/home/">%s </a><br/>' \
                % (thanks_msg, redirect_to_home_msg)
        result = {'result': 1, 'html': html}
        return HttpResponse(json.dumps(result))


@csrf_exempt
def payment(request):
    if request.is_ajax():
        swal_type = 'success'
        text = 'پرداخت شما با موفقیت ارسال شد.'
        html = '<p class="swal-text alert alert-success" style>%s</p>' % text
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        mobileNo = request.POST.get("mobileNo", "")
        national_code = request.POST.get("national_code", "")
        amount = request.POST.get("amount", "")
        if not name or not email or not amount or not national_code or not mobileNo:
            swal_type = 'error'
            text = 'لطفا فرم را کامل کنید.'
            html = '<p class="swal-text alert alert-danger" style>%s</p>' % text
        result = {'html': html, 'swal_type': swal_type}
        return HttpResponse(json.dumps(result))
    return render(request, 'payment.html', {})


@csrf_exempt
def home(request):
    return render(request, 'home.html', {})


@csrf_exempt
def contact_us(request):
    if request.is_ajax():
        swal_type = 'success'
        text = 'درخواست شما با موفقیت ارسال شد.'
        html = '<p class="swal-text alert alert-success" style>%s</p>' % text
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        message = request.POST.get("message", "")
        if not name or not email  or not message:
            swal_type = 'error'
            text = 'لطفا فرم را کامل کنید.'
            html = '<p class="swal-text alert alert-danger" style>%s</p>' % text
        result = {'html': html, 'swal_type':swal_type}
        return HttpResponse(json.dumps(result))

    return  render(request, 'contact_us.html', {})
