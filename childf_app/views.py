import json

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login
from django.core.exceptions import PermissionDenied
from django.forms.widgets import HiddenInput
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
from childf_app.models import HamYar, BonyadPayment, MadadJou, Message, HelpRequest, MadadPayment


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})

class MainPageView(TemplateView):
    template_name = "mainpage.html"


class DevelopmentTeamView(TemplateView):
    template_name = "development_team.html"


class HistoryView(TemplateView):
    template_name = "history.html"


class OrganizationalChart(TemplateView):
    template_name = 'organizational_chart.html'


class GoalsView(TemplateView):
    template_name = 'goals.html'


class ActivitiesView(TemplateView):
    template_name = 'activities.html'


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
            return redirect(reverse('login'))
        except:
            return render(request, 'registration.html', {})
    return PermissionDenied


class AcceptRegistrationTerms(TemplateView):
    template_name = 'accept_registration_terms.html'


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


class BonyadPaymentView(CreateView):
    model = BonyadPayment
    fields = ['amount', 'payer']
    template_name = 'payment.html'
    success_url = reverse_lazy('homepage')

    def get_form(self, form_class=None):
        form = super(BonyadPaymentView, self).get_form(form_class=form_class)
        form.fields['payer'].widget = HiddenInput()
        return form

    def get_initial(self):
        initial = super(BonyadPaymentView, self).get_initial()
        initial['payer'] = self.request.user
        return initial


class DashboardMixin:
    def get(self, request, *args, **kwargs):
        user = request.user
        request.is_hamyar = False
        request.is_madadkar = False
        request.is_madadjou = False
        if hasattr(user, 'hamyar'):
            request.is_hamyar = True
        if hasattr(user, 'madadkar'):
            request.is_madadkar = True
        if hasattr(user, 'madadjou'):
            request.is_madadjou = True
        # print(request.is_hamyar, request.is_madadkar, request.is_madadjou)
        return super(DashboardMixin, self).get(request, *args, **kwargs)


class HomepageView(DashboardMixin, TemplateView):
    template_name = 'afterLogin/homepage.html'


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


class ShowPoorChildrenView(DashboardMixin, ListView):
    template_name = 'afterLogin/show_poor_children.html'
    model = MadadJou
    context_object_name = 'poor_children_list'


@method_decorator(csrf_exempt, name='dispatch')
class SupportChild(FormView):
    success_url = '/show_poor_children'

    def post(self, request, *args, **kwargs):
        pk = request.POST['madadjou_id']
        print("pk",pk)
        madadjou = MadadJou.objects.get(id=pk)
        self.request.user.hamyar.supported_children.add(madadjou)
        return redirect(self.success_url)


class SupportedChildrenView(DashboardMixin, ListView):
    model = MadadJou
    template_name = 'afterLogin/supported_children.html'
    context_object_name = 'poor_children_list'

    def get_queryset(self):
        return self.request.user.hamyar.supported_children.all()

class NewMessageView(DashboardMixin, CreateView):
    model = Message
    fields = '__all__'
    template_name = 'madadJo/send_letter_to_hamyar.html'
    success_url = reverse_lazy('outbox')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['sender'].widget = HiddenInput()
        return form

    def get_initial(self):
        initial = super().get_initial()
        initial['sender'] = self.request.user
        return initial

class InboxView(DashboardMixin, ListView):
    model = Message
    template_name = 'afterLogin/inbox.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return self.request.user.inbox.all()

class OutboxView(DashboardMixin, ListView):
    model = Message
    template_name = 'afterLogin/outbox.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return self.request.user.outbox.all()



class InformationPoorChildren(DashboardMixin, DetailView):
    model = MadadJou
    template_name = 'afterLogin/information_poor_children.html'
    context_object_name = 'madadjou'

@csrf_exempt
def pay_to_selected_children(request):
    return render(request, 'afterLogin/pay_to_selected_children.html', {})


class RegisterPoorChildrenView(DashboardMixin, CreateView):
    template_name = 'afterLogin_madadkar/register_poor_children.html'
    model = MadadJou
    fields = '__all__'
    success_url = reverse_lazy('homepage')


class ShowUnVerifiedRequests(DashboardMixin, ListView):
    model = HelpRequest
    template_name = 'afterLogin/inbox.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return self.model.objects.filter(is_verified=False)


@method_decorator(csrf_exempt, name='dispatch')
class VerifyRequest(FormView):
    success_url = '/'

    def post(self, request, *args, **kwargs):
        pk = request.POST['request_id']
        help_request = HelpRequest.objects.get(id=pk)
        help_request.is_verified = True
        help_request.save()
        return redirect(self.success_url)


class HamyarSupportedChildrenView(DashboardMixin, ListView):
    model = MadadJou
    template_name = 'afterLogin/supported_children.html'
    context_object_name = 'supported_children'

    def get_queryset(self):
        return self.request.user.hamyar.supported_children.all()


class ChildHelpRequestsListView(DashboardMixin, DetailView):
    model = MadadJou
    template_name = 'afterLogin/help_requests.html'
    context_object_name = 'child'


class CreatePayment(DashboardMixin, CreateView):
    model = MadadPayment
    fields = ['amount', 'payer', 'help_request']
    template_name = 'payment.html'
    success_url = reverse_lazy('homepage')

    def dispatch(self, request, *args, **kwargs):
        self.help_request = HelpRequest.objects.get(id=kwargs.get('pk'))
        return super(CreatePayment, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['payer'].widget = HiddenInput()
        form.fields['help_request'].widget = HiddenInput()
        return form

    def get_initial(self):
        initial = super().get_initial()
        initial['payer'] = self.request.user
        initial['help_request'] = self.help_request
        return initial
