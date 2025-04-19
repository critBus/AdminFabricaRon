from django.apps import AppConfig


class AppRoneraConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.app_ronera"
    verbose_name="Ronera"

    def ready(self):
        import apps.app_ronera.signals

