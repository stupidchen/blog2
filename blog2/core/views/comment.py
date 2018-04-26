from django.http.response import JsonResponse
from django.views.generic import View
from ..models import Comment


def get_url_param(path):
    seg = path.split('/')
    id = seg[1]
    return {
        'id': id
    }


# TODO
class CommentView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
