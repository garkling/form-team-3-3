from django.urls import path

from . import views

urlpatterns = [
    path('book-catalog/', views.book_catalog, name='book-catalog'),
    path("book-catalog/<book_id>", views.book_page, name='book-page'),

    path('crud/admin-book-list', views.book_list, name='admin-book-list'),
    path('crud/create-book', views.book_form, name='insert-book'),
    path('crud/update-book/<book_uuid>', views.book_form, name='update-book'),
    path('crud/delete-book/<book_uuid>', views.delete_book, name='delete-book')
]
