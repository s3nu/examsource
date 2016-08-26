from __future__ import unicode_literals

import os
from config.settings import *
from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from django.core.files.storage import FileSystemStorage

class Department(models.Model):
    department = models.CharField(max_length=100)
    class_shortName = models.CharField(max_length=100)

class Classes(models.Model):
    department = models.ForeignKey(Department)
    class_num = models.IntegerField()

class Files(models.Model):
    classes = models.ForeignKey(Classes)
    file_name = models.CharField(max_length=300)
    professor_name = models.CharField(max_length=100)
    file_year = models.IntegerField()
    fileobj = models.FileField(verbose_name=file_name)

