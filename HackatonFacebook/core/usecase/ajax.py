# coding: utf-8
import json
from django.http import HttpResponse

__author__ = 'bustamante'


def get_by_ajax(request):
    if request.method == 'GET':
        values = {'ajax_msg': 'Opa devolvendo o ajax'}
        return HttpResponse(content=json.dumps(values), content_type="application/json")
