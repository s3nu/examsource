from __future__ import unicode_literals

from django.apps import AppConfig


class ExamBankConfig(AppConfig):
    name = 'ExamSource.exambank'
    verbose_name = "Bank"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
