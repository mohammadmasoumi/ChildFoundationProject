"""Childf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from childf_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^development_team/', views.development_team, name='development_team'),
    url(r'^history/', views.history, name='history'),
    url(r'^organizational_chart/', views.organizational_chart, name='organizational_chart'),
    url(r'^goals/', views.goals, name='goals'),
    url(r'^activities/', views.activities, name='activities'),
    url(r'^test/', views.test, name='test'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^accept_registration_terms/', views.accept_registration_terms, name='accept_registration_terms'),
    url(r'^activation_code/$', views.activation_code, name='activation_code'),
    url(r'^sms/$', views.resend_sms, name='resend_sms'),
    url(r'^login/$', views.login, name='login'),
    url(r'^verification/$', views.verification, name='verification'),
    url(r'^payment/$', views.payment, name='payment'),
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^forget_password/$', views.forget_password, name='forget_password'),
    url(r'^userprofile/$', views.userprofile, name='userprofile'),
    url(r'^userpayment/$', views.userpayment, name='userpayment'),
    url(r'^show_poor_children/$', views.show_poor_children, name='show_poor_children'),
    url(r'^supported_children/$', views.supported_children, name='supported_children'),
    url(r'^trans_history/$', views.trans_history, name='trans_history'),
    url(r'^letters/$', views.letters, name='letters'),
    url(r'^information_poor_children/(?P<children_id>\d+)/$', views.information_poor_children, name='information_poor_children'),
    url(r'^information_poor_children/$', views.information_poor_children, name='information_poor_children'),
    url(r'pay_to_selected_children/$', views.pay_to_selected_children, name='pay_to_selected_children'),
    url(r'madadkar_dashboard/$', views.madadkar_dashboard, name='madadkar_dashboard'),
    url(r'register_poor_children/$', views.register_poor_children, name='register_poor_children'),


]
