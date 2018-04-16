from django.urls import path

from . import views

urlpatterns = [
    path('<str:username>', views.index, name='index'),
    path('archive/<str:id>/', views.archive, name='archive_id'),
    path('archive/', views.archive, name='archive_id' ),
    path('user/<str:id>/', views.user, name='user_id'),
    path('user/', views.user, name='user_id'),
]
