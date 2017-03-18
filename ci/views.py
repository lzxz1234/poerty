#!/usr/bin/python
# coding=utf-8

from models import Ci
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template


def ci(request):
    key = request.GET.get('key')
    page = int(request.GET.get('page') if request.GET.get('page') else '1')
    size = int(request.GET.get('size') if request.GET.get('size') else '10')
    t = get_template('ci.html')
    ci_list = Ci.objects.all()
    if key:
        ci_list = ci_list.filter(content__contains=key)
    html = t.render(Context({
        'list': ci_list[page*size-size:page*size],
        'request': request,
        'pages': ci_list.count() / size,
        'page': page,
        'key': key,
        'size': size
    }))
    return HttpResponse(html)
