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

    # url(r'^$', views.homepage, name='homepage')
    # url(r'^$', views.homepage, name='homepage')
#    url(r'^login/', views.login, name='login')
    # url(r'^registration/', views.registration, name='registration')
    # url(r'^join-to-the-Institute/', views.join_to_the_Institute, name='join_to_the-_Institute')
    # url(r'^Introduction-to-the-Institute/', views.Introduction_to_the_Institute, name='Introduction_to_the_Institute')
    # url(r'^homepage', views.homepage, name='homepage')
    #



    # url(r'^/', admin.site.urls),
]
