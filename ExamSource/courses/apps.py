from django.apps import AppConfig


class CoursesConfig(AppConfig):
    name = 'ExamSource.courses'
    verbose_name = "courses"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
