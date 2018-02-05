from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls.base import reverse
import requests
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from childf_app.models import HamYar


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
    if request.method == 'GET':
        return render(request, 'registration.html', {})
    if request.method == 'POST':
        try:
            print(request.POST)
            HamYar.objects.create(username=request.POST.get('username'),
                                  first_name=request.POST.get('first_name'),
                                  last_name=request.POST.get('last_name'),
                                  code_melli=request.POST.get('code_melli'),
                                  job=request.POST.get('job'),
                                  gender=request.POST.get('gender'),
                                  education=request.POST.get('education'),
                                  password=request.POST.get('password'),
                                  email=request.POST.get('email'),
                                  payment_period=request.POST.get('payment_period'),
                                  )
            return redirect(reverse('mainpage'))
        except:
            return render(request, 'registration.html', {})
    return PermissionDenied


def accept_registration_terms(request):
    return render(request, 'accept_registration_terms.html', {})


@csrf_exempt
def activation_code(request):
    return render(request, 'activation_code.html', {})


@csrf_exempt
def resend_sms(request):
    text = 'کد فعال سازی ارسال شد'
    html = '<p class="swal-text">%s</p>' % text
    return HttpResponse(html)


@csrf_exempt
def send_code(request):
    mobileNo = 123
    resend_sms(mobileNo)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/homepage')
    return render(request, 'login.html', {})


@csrf_exempt
def verification(request):
    if request.is_ajax():
        entered_code = request.POST.get('code', False)
        thanks_msg = ("حساب کاربری شما با موفقیت ساخته شد!")
        redirect_to_home_msg = ("صفحه اصلی خود را ببینید")
        html = '<p class="swal-text">%s</p>' \
               ' <hr> <a class="swal-text" href="/homepage/">%s </a><br/>' \
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
def homepage(request):
    return render(request, 'afterLogin/homepage.html', {})


@csrf_exempt
def contact_us(request):
    if request.is_ajax():
        swal_type = 'success'
        text = 'درخواست شما با موفقیت ارسال شد.'
        html = '<p class="swal-text alert alert-success" style>%s</p>' % text
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        message = request.POST.get("message", "")
        if not name or not email or not message:
            swal_type = 'error'
            text = 'لطفا فرم را کامل کنید.'
            html = '<p class="swal-text alert alert-danger" style>%s</p>' % text
        result = {'html': html, 'swal_type': swal_type}
        return HttpResponse(json.dumps(result))

    return render(request, 'contact_us.html', {})


@csrf_exempt
def forget_password(request):
    if request.is_ajax():
        swal_type = 'success'
        text = 'ایمیل تغیر کلمه عبور برای شما ارسال شد.'
        html = '<p class="swal-text alert alert-success" style>%s</p>' % text
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        if not username or not email:
            swal_type = 'error'
            text = 'لطفا فرم را کامل کنید.'
            html = '<p class="swal-text alert alert-danger" style>%s</p>' % text
        result = {'html': html, 'swal_type': swal_type}
        return HttpResponse(json.dumps(result))

    return render(request, 'forget_password.html', {})


@csrf_exempt
def userprofile(request):
    return render(request, 'afterLogin/userprofile.html', {})


@csrf_exempt
def userpayment(request):
    return render(request, 'afterLogin/userpayment.html', {})


selected_children = []


@csrf_exempt
def show_poor_children(request):
    print(request.method)
    if request.is_ajax():
        if request.method == "GET":
            selected_children.clear()
        else:
            selected_children.append(request.POST.get['id'])

    return render(request, 'afterLogin/show_poor_children.html', {})


@csrf_exempt
def supported_children(request):
    return render(request, 'afterLogin/supported_children.html', {})


@csrf_exempt
def trans_history(request):
    return render(request, 'afterLogin/trans_history.html', {})


@csrf_exempt
def letters(request):
    return render(request, 'afterLogin/letters.html', {})


@csrf_exempt
def information_poor_children(request, children_id):
    if True:
        id = 1
        name = 'علی'
        sex = 'مذکر'
        age = 16
        birth_day = '1380/12/16'
        physical_condition = 'سالم'
        type_of_disease = ''
        general_condition = 'سالم'

        address = 'تهران-ورامین'
        housing_ownership = 'استیجاری'
        number_of_rooms = 1
        rent_of_house = 12000000
        residence_status = 'محمد به همراه برادرش در خانه زندگی میکنند'

        father_employment_status = 'بی کار'
        father_income_per_month = 0
        father_job = ''
        mother_employment_status = 'بی کار'
        mother_income_per_month = 0
        mother_job = ''
        help_from_foreign_source = 'خیر'
        foregin_source = ''
        income_from_foreign_source = 0
        decription = 'نیازمند کمک فوری'

        mother_education = 'بی سواد'
        mother_birthday = '1357/12/16'
        mother_physical_condition = 'سالم'
        mother_type_of_disease = ''
        the_cause_of_death_or_lack_of_mother = ''

        father_education = 'بی سواد'
        father_birthday = '1354/12/16'
        father_physical_condition = 'سالم'
        father_type_of_disease = ''
        the_cause_of_death_or_lack_of_father = ''

        household_head = 'پدر'
        number_of_sister = 0
        number_of_brother = 1

        content = {
            'id': id,
            'name': name,
            'sex': sex,
            'age': age,
            'birth_day': birth_day,
            'physical_condition': physical_condition,
            'type_of_disease': type_of_disease,
            'general_condition': general_condition,

            'address': address,
            'housing_ownership': housing_ownership,
            'number_of_rooms': number_of_rooms,
            'rent_of_house': rent_of_house,
            'residence_status': residence_status,

            'father_employment_status': father_employment_status,
            'father_income_per_month': father_income_per_month,
            'father_job': father_job,
            'mother_employment_status': mother_employment_status,
            'mother_income_per_month': mother_income_per_month,
            'mother_job': mother_job,
            'help_from_foreign_source': help_from_foreign_source,
            'foregin_source': foregin_source,
            'income_from_foreign_source': income_from_foreign_source,
            'decription': decription,

            'mother_education': mother_education,
            'mother_birthday': mother_birthday,
            'mother_physical_condition': mother_physical_condition,
            'mother_type_of_disease': mother_type_of_disease,
            'the_cause_of_death_or_lack_of_mother': the_cause_of_death_or_lack_of_mother,
            'father_education': father_education,
            'father_birthday': father_birthday,
            'father_physical_condition': father_physical_condition,
            'father_type_of_disease': father_type_of_disease,
            'the_cause_of_death_or_lack_of_father': the_cause_of_death_or_lack_of_father,

            'household_head': household_head,
            'number_of_sister': number_of_sister,
            'number_of_brother': number_of_brother,
        }

        return render(request, 'afterLogin/information_poor_children.html', content)

    return render(request, 'afterLogin/information_poor_children.html', {})


@csrf_exempt
def pay_to_selected_children(request):
    return render(request, 'afterLogin/pay_to_selected_children.html', {})


@csrf_exempt
def madadkar_dashboard(request):
    return render(request, 'afterLogin_madadkar/dashboard.html', {})


@csrf_exempt
def register_poor_children(request):
    return render(request, 'afterLogin_madadkar/register_poor_children.html')


@csrf_exempt
def supported_children_madadkar(request):
    return render(request, 'afterLogin_madadkar/supported_children_madadkar.html')


@csrf_exempt
def letters_madadkar(request):
    return render(request, 'afterLogin_madadkar/letters.html')


@csrf_exempt
def trans_history_madadJo(request):
    return render(request, 'madadJo/trans_history_madadJo.html')


@csrf_exempt
def madadjo_dashboard(request):
    return render(request, 'madadJo/dashboard.html')


@csrf_exempt
def submit_req_to_madadkar(request):
    return render(request, 'madadJo/submit_req_to_madadkar.html')


@csrf_exempt
def submit_change_req_for_madadkar(request):
    return render(request, 'madadJo/submit_change_req_for_madadkar.html')


@csrf_exempt
def send_letter_to_hamyar(request):
    return render(request, 'madadJo/send_letter_to_hamyar.html')


@csrf_exempt
def send_letter_to_madadkar(request):
    return render(request, 'madadJo/send_letter_to_madadkar.html')


@csrf_exempt
def show_poor_children_madadkar(request):
    return render(request, 'afterLogin_madadkar/show_poor_children.html')

