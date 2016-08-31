# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import  Document
from .forms import DocumentForm

def list(request):
    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'exambank/base.html',
        {'documents': documents}
    )
