from django.apps import AppConfig


class ChildfAppConfig(AppConfig):
    name = 'childf_app'
    verbose_name = 'Childf'

    def ready(self):
        print('Child Foundation Project Start')