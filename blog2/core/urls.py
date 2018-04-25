from django.urls import path

#from .views.method_views import *
from .views.archive import ArchiveView
from .views.user import UserView

app_name = 'core'
urlpatterns = [
    # path('archive/', views.archive, name='archive'),
    # path('archive/<str:aid>/', views.archive, name='archive_detail'),
    # path('user/', views.user, name='user'),
    # path('user/login', views.login, name='login'),
    # path('user/logout', views.logout, name='logout'),
    # path('user/<str:uid>/', views.user, name='user_detail'),
    # path('index/<str:uid>', views.index, name='index'),
    path('archive<path:path>', ArchiveView.as_view(), name='archive'),
    path('user<path:path>', UserView.as_view(), name='user'),
]
