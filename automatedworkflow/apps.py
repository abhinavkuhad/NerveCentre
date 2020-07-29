from django.apps import AppConfig


class AutomatedworkflowConfig(AppConfig):
    name = 'automatedworkflow'

    def ready(self):
        from schedulers import scheduler
        scheduler.start()
