from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.all_books, name='all-books'),
    path("books/<book_id>", views.book_page, name='book-page'),
]
