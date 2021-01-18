from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('sign-in', views.register, name='sign-in'),
    path('login', views.log_in, name='log-in'),
    path('activation', views.change_status, name='activation'),
    path('logout', views.user_logout, name='log-out')
]
