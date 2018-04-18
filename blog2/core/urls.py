from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('archive/', views.archive, name='archive'),
    path('archive/<str:id>/', views.archive, name='archive_id'),
    path('user/', views.user, name='user'),
    path('user/<str:id>/', views.user, name='user_id'),
    path('index/<str:username>', views.index, name='index'),
]
