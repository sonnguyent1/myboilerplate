from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "auth_service.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals
        except ImportError:
            pass
