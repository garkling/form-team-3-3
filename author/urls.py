from django.urls import path

from . import views

urlpatterns = [
    path('author-catalog/', views.author_catalog, name='author-catalog'),
    path('author-catalog/<author_id>', views.author_page, name='author-page'),

    path('crud/admin-author-list', views.author_list, name='admin-author-list'),
    path('crud/create-author', views.author_form, name='insert-author'),
    path('crud/update-author/<author_uuid>', views.author_form, name='update-author'),
    path('crud/delete-author/<author_uuid>', views.delete_author, name='delete-author')
]
