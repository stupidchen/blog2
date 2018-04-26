from django.http.response import JsonResponse
from django.views.generic import View
from ..models import User


def get_url_param(path):
    seg = path.split('/')
    id = seg[1]
    return {
        'id': id
    }


# TODO
class UserView(View):
    def get(self, request, path):
        if path == '/':
            users = User.objects.all()
            data = [user.as_dict() for user in users]
            return JsonResponse({
                'data': data
            })
        else:
            user = User.objects.get(pk=get_url_param(path)['id'])
            data = user.as_dict()
            return JsonResponse({
                'data': data
            })

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
