from datetime import datetime
import uuid

from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse

from ..models import Archive
from ..utils import get_current_user, Error


def get_url_param(path):
    seg = path.split('/')
    id = seg[1]
    return {
        'id': id
    }


def get_query_param(path):
    query_params = path.split('?')[1].split('&')
    ret = object()
    for params in query_params:
        kv = params.split('=')
        ret.__setattr__(kv[0], kv[1])
    return ret


class ArchiveView(View):
    def get(self, request, path=None):
        if path == '/':
            archives = Archive.objects.order_by('-pubTime')
            data = [archive.as_dict() for archive in archives]
            return JsonResponse({
                'error': Error.NO_ERROR,
                'data': data
            })
        else:
            archive = Archive.objects.get(pk=get_url_param(path)['id'])
            data = archive.as_dict()
            return JsonResponse({
                'error': Error.NO_ERROR,
                'data': data
            })

    def post(self, request, path=None):
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = get_current_user()
        id = get_url_param(path)['id']
        if id is None:
            aid = str(uuid.uuid4()).replace('-', '')
            pubTime = datetime.now()
            editTime = pubTime
            new_archive = Archive(aid=aid, title=title, content=content, pubTime=pubTime, editTime=editTime,
                                  author=author)
            new_archive.save()
            return JsonResponse({
                'error': Error.NO_ERROR,
            })
        else:
            archive = get_object_or_404(Archive, pk=id)
            archive.title = title
            archive.content = content
            editTime = datetime.now()
            archive.editTime = editTime
            archive.save()
            return HttpResponseRedirect(reverse('core:archive', args=(id,)))
        pass

    def put(self, request, path=None):
        pass

    def delete(self, request, path=None):
        pass
