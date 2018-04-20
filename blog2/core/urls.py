from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('archive/', views.archive, name='archive'),
    path('archive/<str:aid>/', views.archive, name='archive_detail'),
    path('user/login', views.login, name='user_login'),
    path('user/logout', views.logout, name='user_logout'),
    path('user/<str:uid>/', views.user, name='user_detail'),
    path('index/<str:uid>', views.index, name='index'),
]
