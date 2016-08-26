# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

# urlpatterns = [
#     url(
#         regex=r'^$',
#         view=views.list,
#         name='list'
#     ),
    # if settings.DEBUG:
    #     urlpatterns += staticfiles_urlpatterns()  # this serves static files and media files.
    # # in case media is not served correctly
    #     urlpatterns += patterns('',
    #     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    # ),
# ]

urlpatterns = [
    url(r'^dept/$', views.departmentList, name='department'),
    #url(r'^/([0-9]{3})/$', views.classList, name='classes'),
    url(r'^(\d+)/$', views.classList, name='classList'),
    #url(r'^list/$', views.list, name='list'),
]

