from __future__ import unicode_literals

import os
from config.settings import *
from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from django.core.files.storage import FileSystemStorage

class Bank(models.Model):
    department = models.CharField(max_length=20)
    class_name = models.CharField(max_length=10)
    class_num = models.IntegerField()
    file_name = models.CharField(max_length=30, default='.pdf')

class Document(models.Model):
    docfile = models.FileField()
