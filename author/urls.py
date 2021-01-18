from django.urls import path

from . import views

urlpatterns = [
    path('authors/', views.all_authors, name='all-authors'),
    path('authors/<author_id>', views.author_page, name='author-page'),
]
