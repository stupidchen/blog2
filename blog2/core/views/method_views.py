from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from datetime import datetime
from blog2.core.models import Archive
from blog2.core.models import User
from blog2.core.utils import get_current_user
from blog2.core.utils import Tokens
import uuid


def index(request, **kwargs):
    latest_archive = Archive.objects.order_by('-pubTime')[:5]
    context = {
        'archives': latest_archive,
        'username': kwargs.get('username'),
    }
    return render(request, 'core/index.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            match_user = User.objects.get(username=username, password=password)
        except:
            raise PermissionDenied

        token = uuid.uuid4()
        Tokens.set_token(token, match_user.id)
        context = {
            'token': token,
        }
        return render(request, 'core/login.html', context)

    if request.method == 'GET':
        return render(request, 'core/login.html')


def logout(request):
    token = request.POST['token']
    try:
        uid = Tokens.get_uid(token)
    except:
        raise PermissionDenied

    Tokens.remove_token(token)
    return HttpResponseRedirect(reverse('core:archive'))


def user(request, uid=None):
    if request.method == 'GET':
        users = User.objects.all()
        context = {
            users: users
        }
        return render(request, 'core/users.html', context)

    if request.method == 'POST':
        pass

    if request.method == 'DELETE':
        pass

    if request.method == 'PUT':
        pass


def archive(request, aid=None, limit=10):
    if request.method == 'GET':
        if aid is None:
            latest_archives = Archive.objects.order_by('-pubTime')[:limit]
            context = {
                'archives': latest_archives,
            }
            return render(request, 'core/archives.html', context)
        else:
            archive = get_object_or_404(Archive, pk=aid)
            context = {
                'archive': archive,
            }
            return render(request, 'core/archive.html', context)

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = get_current_user()
        if aid is None:
            aid = str(uuid.uuid4()).replace('-', '')
            pubTime = datetime.now()
            editTime = pubTime
            new_archive = Archive(aid=aid, title=title, content=content, pubTime=pubTime, editTime=editTime,
                                  author=author)
            new_archive.save()
            return HttpResponseRedirect(reverse('core:archive'))
        else:
            archive = get_object_or_404(Archive, pk=aid)
            archive.title = title
            archive.content = content
            editTime = datetime.now()
            archive.editTime = editTime
            archive.save()
            return HttpResponseRedirect(reverse('core:archive_detail', args=(aid,)))
