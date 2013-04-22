# (c) Fugro.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals
from __future__ import print_function

from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.conf import settings

gs_setting = getattr(settings, 'IMPORTER_GEOSERVER')


def showshow(request):
    request_string = request.get_full_path()
    host = gs_setting['geoserver_url']
    work_space = gs_setting['geoserver_workspace']

    user_name = request.user.username
    if request_string.find('&viewparams=usr:') != -1:
        raise PermissionDenied
    new_req_string = request_string + '&viewparams=usr:'
    new_req_string += user_name

    new_url = host + '/' + work_space + '/' + new_req_string
    new_url = new_url.replace('/?', '?')
    return HttpResponse('<img src="' + new_url + '" />')
