from django.shortcuts import render
from .models import Archive

# Create your views here.

def index(request, **kwargs):
    latest_archive = Archive.objects.order_by('-pubTime')[:5]
    context = {
        'latest_archive_list': latest_archive,
    }
    return render(request, 'core/index.html', context)


def user(request, username):
    pass

def archive(request, id):
    pass