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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.auth import views as auth_views

from childf_app import views
from childf_app.views import BonyadPaymentView, HomepageView, RegisterPoorChildrenView, signup, \
    MainPageView, DevelopmentTeamView, OrganizationalChart, HistoryView, GoalsView, ActivitiesView, \
    AcceptRegistrationTerms, ShowPoorChildrenView, SupportChild, SupportedChildrenView, \
    InformationPoorChildren, NewMessageView, OutboxView, InboxView, ChildHelpRequestsListView, \
    CreatePayment

urlpatterns = \
    [url(r'^admin/', admin.site.urls),
     url(r'^$', MainPageView.as_view(), name='mainpage'),
     url(r'^development_team/', DevelopmentTeamView.as_view(),
         name='development_team'),
     url(r'^history/', HistoryView.as_view(), name='history'),
     url(r'^organizational_chart/', OrganizationalChart.as_view(),
         name='organizational_chart'),
     url(r'^goals/', GoalsView.as_view(), name='goals'),
     url(r'^activities/', ActivitiesView.as_view(), name='activities'),
     url(r'^registration/$', views.registration, name='registration'),
     url(r'^accept_registration_terms/', AcceptRegistrationTerms.as_view(),
         name='accept_registration_terms'),
     url(r'^activation_code/$', views.activation_code, name='activation_code'),
     url(r'^sms/$', views.resend_sms, name='resend_sms'),
     url(r'^login/$', auth_views.login, name='login'),
     url(r'^logout/$', auth_views.logout, name='logout'),
     url(r'^signup/$', signup, name='signup'),
     url(r'^verification/$', views.verification, name='verification'),
     url(r'^payment/$', BonyadPaymentView.as_view(), name='payment'),
     # dash board
     url(r'^homepage/$', HomepageView.as_view(), name='homepage'),
     url(r'^contact_us/$', views.contact_us, name='contact_us'),
     url(r'^forget_password/$', views.forget_password, name='forget_password'),
     url(r'^userprofile/$', views.userprofile, name='userprofile'),
     url(r'^show_poor_children/$', ShowPoorChildrenView.as_view(),
         name='show_poor_children'),
     # url(r'^show_poor_children/$', ShowPoorChildrenView.as_view(), name='show_poor_children'),
     url(r'^supported_children/$', SupportedChildrenView.as_view(),
         name='supported_children'),
     url(r'^support_child/$', SupportChild.as_view(),
         name='support_child'),
     url(r'^information_poor_children/(?P<pk>\d+)/$',
         InformationPoorChildren.as_view(), name='information_poor_children'),
     url(r'pay_to_selected_children/$', views.pay_to_selected_children,
         name='pay_to_selected_children'),
     url(r'register_poor_children/$', RegisterPoorChildrenView.as_view(),
         name='register_poor_children'),
     url(r'send_letter_to_hamyar/$', NewMessageView.as_view(),
         name='send_letter_to_hamyar'),
     url(r'outbox/$', OutboxView.as_view(), name='outbox'),
     url(r'inbox/$', InboxView.as_view(), name='inbox'),
     url(r'child/(?P<pk>\d+)/$', ChildHelpRequestsListView.as_view(), name='help_requests'),
     url(r'help/(?P<pk>\d+)/$', CreatePayment.as_view(), name='help'),
     ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
