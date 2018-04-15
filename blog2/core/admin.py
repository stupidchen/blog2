from django.contrib import admin

# Register your models here.
from .models import User, Archive, Comment
admin.site.register(User)
admin.site.register(Archive)
admin.site.register(Comment)