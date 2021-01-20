from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='main'),
    path('sign-in', views.register, name='sign-in'),
    path('login', views.log_in, name='log-in'),
    path('activation', views.change_status, name='activation'),
    path('logout', views.user_logout, name='log-out'),

    path('crud/admin-user-list', views.user_list, name='admin-user-list'),
    path('crud/create-user', views.user_form, name='insert-user'),
    path('crud/update-user/<user_uuid>', views.user_form, name='update-user'),
    path('crud/delete-user/<user_uuid>', views.delete_user, name='delete-user'),
]
