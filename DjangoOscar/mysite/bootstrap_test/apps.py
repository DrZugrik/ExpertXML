from django.apps import AppConfig


class BootstrapTestConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bootstrap_test"

class MySiteConfig(AppConfig):
    name = 'mysite'

    def ready(self):
        import mysite.signals