from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Archive

# Create your views here.

def index(request, **kwargs):
    latest_archive = Archive.objects.order_by('-pubTime')[:5]
    context = {
        'latest_archive_list': latest_archive,
        'username': kwargs.get('username'),
    }
    return render(request, 'core/index.html', context)


def user(request, username):
    pass

def archive(request, id, limit=10):
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
