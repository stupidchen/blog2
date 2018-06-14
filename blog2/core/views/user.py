import json
import uuid

from django.http.response import JsonResponse
from django.views.generic import View

from ..models import User
from ..utils import Tokens
from ..utils import Error


def get_url_param(path):
    seg = path.split('/')
    id = seg[1]
    return {
        'id': id
    }


class UserView(View):
    @staticmethod
    def get(request, path):
        if path == '/':
            users = User.objects.all()
            data = [user.as_dict() for user in users]
            return JsonResponse({
                'data': data
            })

        user = User.objects.get(pk=get_url_param(path)['id'])
        data = user.as_dict()
        return JsonResponse({
            'error': Error.NO_ERROR,
            'data': data,
        })

    @staticmethod
    def post(request, path):
        data = json.loads(request.POST.get('data'))

        if path == '/login':

            username = data['username']
            password = data['password']
            try:
                match_user = User.objects.get(username=username, password=password)
            except:
                return JsonResponse({
                    'error': Error.USERNAME_OR_PASSWORD_INCORRECT,
                })

            token = uuid.uuid4()
            Tokens.set_token(token, match_user.id)
            return JsonResponse({
                'error': Error.NO_ERROR,
                'token': token,
            })

        if path == '/logout':
            token = request.POST.get('token')
            try:
                uid = Tokens.get_uid(token)
            except:
                return JsonResponse({
                    'error': Error.TOKEN_INVALID,
                })

            Tokens.remove_token(token)
            return JsonResponse({
                'error': Error.NO_ERROR,
            })

        if path == '/register':
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            information = data.get('information')
            if username is None or password is None:
                return JsonResponse({
                    'error': Error.USERNAME_OR_PASSWORD_CANNOT_BE_NULL
                })
            id = str(uuid.uuid4()).replace('-', '')
            new_user = User(id=id, username=username, email=email, password=password, information=information)
            new_user.save()
            return JsonResponse({
                'error': Error.NO_ERROR,
            })

        return JsonResponse({
            'error': Error.INVALID_PATH,
        })

    def put(self, request, path):
        pass

    def delete(self, request, path):
        pass
