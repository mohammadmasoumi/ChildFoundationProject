from django.conf.urls import url, include
from django.contrib import admin
from rest_app import views

urlpatterns = [
    # # TODo must create functions in views

    url(r'^signin/', views.signin),
    url(r'^signup/', views.signup),
    url(r'^generate_token/', views.generate_token),
    # url(r'^cash_out_order/', views.cash_out_order, name='cash_out'),
    # url(r'^get_order_status/', views.get_order_status, name='order_status'),
    # url(r'^cash_out_reversal/', views.cash_out_reversal, name='cash_out_reversal'),
    # url(r'^get_pending_orders/', views.get_pending_orders, name='get_pending_orders'),
    # url(r'^get_paid_orders/', views.get_paid_orders),
    # url(r'^get_expired_orders/', views.get_expired_orders),
]
