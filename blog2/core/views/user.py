from django.http.response import HttpResponse
from django.views.generic import View
from ..models import User

class UserView(View):
	def get(self, request, path):
		return HttpResponse("Hello user! %s" % path)

	def post(self, request):
		pass

	def put(self, request):
		pass

	def delete(self, request):
		pass