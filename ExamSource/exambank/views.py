# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Department, Classes

# def list(request):
#     # Load documents for the list page
#     documents = Document.objects.all()
#
#     # Render list page with the documents and the form
#     return render(
#         request,
#         'exambank/base.html',
#         {'documents': documents}
#     )

def departmentList(request):
    departments = Department.objects.all()

    return render(
        request,
        'exambank/department.html',
        {'departments': departments}
    )

def classList(request, deptId):
    classes = Classes.objects.get(department_id=deptId)

    return reverse('classList',
                   kwargs={'cls': deptId})
    # return render(
    #     request,
    #     'exambank/classes.html',
    #     {'classes': classes}
    # )
