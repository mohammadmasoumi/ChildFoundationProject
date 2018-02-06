from django.contrib import admin

# Register your models here.

# Register your models here.
from django.contrib import admin
from childf_app import models
from childf_app.utils import *


class MadadJouAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'shomare_parvande', ]
    list_filter = ['user',]

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'username'


class MadadKarAdmin(admin.ModelAdmin):
    list_display = ['get_username']
    list_filter = ['user']

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'username'


class HamYarAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'code_melli','get_relation', ]
    list_filter = ['user', 'supported_children']

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'username'

    def get_relation(self, obj):
        return obj.supported_children

    get_relation.short_description = 'supported_children'

admin.site.register(models.MadadJou, MadadJouAdmin)
admin.site.register(models.MadadKar, MadadKarAdmin)
admin.site.register(models.HamYar, HamYarAdmin)

