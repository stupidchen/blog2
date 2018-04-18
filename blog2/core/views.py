from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .models import Archive
from .utils import get_current_user
import uuid

# Create your views here.

def index(request, **kwargs):
    latest_archive = Archive.objects.order_by('-pubTime')[:5]
    context = {
        'archives': latest_archive,
        'username': kwargs.get('username'),
    }
    return render(request, 'core/index.html', context)

def user(request, username):
    pass

def archive(request, id=None, limit=10):
    if request.method == 'GET':
        if id is None:
            latest_archives = Archive.objects.order_by('-pubTime')[:limit]
            context = {
                'archives': latest_archives,
            }
            return render(request, 'core/archives.html', context)
        else:
            archive = get_object_or_404(Archive, pk=id)
            context = {
                'archive': archive,
            }
            return render(request, 'core/archive.html', context)

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = get_current_user()
        if id is None:
            id = str(uuid.uuid4()).replace('-', '')
            pubTime = datetime.now()
            editTime = pubTime
            new_archive = Archive(id=id, title=title, content=content, pubTime=pubTime, editTime=editTime, author=author)
            new_archive.save()
            return HttpResponseRedirect(reverse('core:archive'))
        else:
            archive = get_object_or_404(Archive, pk=id)
            archive.title = title
            archive.content = content
            editTime = datetime.now()
            archive.editTime = editTime
            archive.save()
            return HttpResponseRedirect(reverse('core:archive_id', args=(id,)))